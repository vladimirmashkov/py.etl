import shutil
import os
import psycopg2
import psycopg2.extras as pg_ext
import sys
import time
import uuid
import re
import pandas as pd

from sqlalchemy import create_engine
from datetime import datetime
from google.protobuf.json_format import MessageToDict
from multiprocessing import Queue, Process

from config import path as path
from config import s2 as src
from config import stage as stage
from config import dwh as dwh

import s2_video_learningVideo.config as pkg
from s2_video_learningVideo.ss import data_import_pb2 as pb2


sfPackageId = pkg.package_uuid
sfPackageFlowId = uuid.uuid4()
sfDateTime = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f +03:00"))
package_name = pkg.package_name
path_temp_files = path()["temp_dir"]
path_work_dir = path()["work_dir"]
file_name_sql = os.path.join(path_work_dir, package_name, "sql", "slc_source.sql")

rows_in_a_batch = pkg.rows_in_a_batch

def src_read():
    print("Data preparation started. file - {file_name_sql}".format(file_name_sql=file_name_sql))
    start = time.time()

    engine_src = create_engine('postgresql://{user}:{password}@{host}:{port}/{database}'.format(
    user=src()["user"],
    password=src()["password"],
    host=src()["host"],
    port=src()["port"],
    database=src()["database"]
    ))

    with open(file_name_sql, 'r') as f:
        prefix = "/* package_uuid: {package_uuid} */\n\r".format(package_uuid = sfPackageId)
        content = f.read()
        content = prefix + content
        sql = content.replace("sfPackageId", sfPackageId)   
   
    df = pd.read_sql_query(sql, engine_src, chunksize=rows_in_a_batch)
    print('Data preparation spent time: {} sec.'.format(round(time.time() - start, 2)))
    return df

def save_to_bin(df_id, df):
    table = pb2.import_s2_video_learningVideo()
    for index, row in df.iterrows():
        # print(row)
        table.row.add (
            id=row["id"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
            uuid=row["uuid"],
            url=row["url"],
            name=row["name"],
            description=row["description"],
            image=row["image"],
            number=row["number"],
            duration_min=row["duration_min"],
            is_popular=row["is_popular"],
            class_id=row["class_id"],
            subject_id=row["subject_id"],
            access_id=row["access_id"],
            sfTableoid=row["sftableoid"],
            sfXmin=row["sfxmin"],
            )
    bytesAsString = table.SerializeToString()
    return bytesAsString

def save_to_files(queue):
    df_chunked = src_read()
    for df_id, df in enumerate(df_chunked):
        bytesAsString = save_to_bin(df_id, df)
        file_name = '{path_temp_files}/{package_name}_{sfPackageFlowId}_{df_id}.bin'.format(
            path_temp_files = path_temp_files,
            package_name = package_name, 
            sfPackageFlowId = sfPackageFlowId,
            df_id = df_id
            )
        with open (file_name, "wb") as f:
            f.write(bytesAsString)       
        queue.put(file_name)
    queue.put(None)  

def read_from_files(file_name):
    with open(file_name, "rb") as f:
        table = pb2.import_s2_video_learningVideo().FromString(f.read())
        dict_obj = MessageToDict(table)
        return dict_obj

def dst_put(dict_obj):

    connection = psycopg2.connect(host=stage()["host"], port=stage()["port"], database=stage()["database"], user=stage()["user"], password=stage()["password"])
    cursor = connection.cursor()
    dic1 = dict_obj["row"]
    # print(dic1)
    pg_ext.execute_batch (cursor, """INSERT INTO ss.S2_video_learningVideo (id, created_at, updated_at, uuid, url, "name", description, image, "number", duration_min, is_popular, class_id, subject_id, access_id, sfDateTime, sfPackageId, sfPackageFlowId, sfTableoid, sfXmin) VALUES (
        %(id)s, %(createdAt)s, %(updatedAt)s, %(uuid)s, %(url)s, %(name)s, %(description)s, %(image)s, %(number)s, %(durationMin)s, %(isPopular)s, %(classId)s, %(subjectId)s, %(accessId)s, '{sfDateTime}', '{sfPackageId}', '{sfPackageFlowId}', %(sfTableoid)s, %(sfXmin)s
    )""".format(sfDateTime=sfDateTime, sfPackageId=sfPackageId, sfPackageFlowId=sfPackageFlowId), dic1)  	

    connection.commit()

def put_file_to_dst(queue):
    start_etl = time.time()
    while True:
        file_name = queue.get()
        if file_name is None:
            print('The total spent time: {sec} sec.'.format(sec = round(time.time() - start_etl, 2)))
            break
        else:
            if os.path.exists(file_name):
                start_put = time.time()
                dict_obj = read_from_files(file_name)
                dst_put(dict_obj)
                os.remove(file_name)
                df_id = int(re.findall('\.[0-9]*_', file_name[::-1])[0].replace(".","").replace("_","")[::-1])
                print ('has been inserted {rows} rows in {sec} sec.'.format(rows = (df_id+1)*rows_in_a_batch, sec = round(time.time() - start_put, 2)))    

def main():
    q = Queue()
    p = Process(target=save_to_files, args=((q),))
    p.daemon = True
    p.start()
    put_file_to_dst(q)
    p.join()

if __name__ == "__main__":
    pass