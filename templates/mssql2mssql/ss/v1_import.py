import shutil
import os
import sys
import time
import uuid
import re
import pandas as pd
import pyodbc
import pymssql
import subprocess
from datetime import datetime
from sqlalchemy import create_engine
from datetime import datetime
from multiprocessing import Queue, Process

from config import s1 as src
from config import path as path
from config import stage as dst

now = datetime.now()
sfDate=str(now.strftime("%Y-%m-%dT%H:%M:%S.%f"))
sfUUID=str(uuid.uuid4())



def data_flow_q():
    schema_name="dbo"
    table_name="telegram_messages"
    with open("{work_dir}/mssql2mssql/sql/src_select.sql".format(work_dir=path()["work_dir"]), 'r') as f: 
        sql = f.read()
    sql = sql.replace('<sfDate>', sfDate).replace('<sfUUID>', sfUUID)
    sql = sql.replace('\n','').replace('\r','').replace('\t','')
    # print(sql)
    bcp_string_src="""bcp "{sql}" queryout "{temp_dir}/{schema_name}.{table_name}.dat" -S "{host},{port}" -U "{user}" -P "{password}" -d "{database}" -T -C RAW -n -E -a 10000""".format(
        schema_name=schema_name,
        table_name=table_name,
        sql=sql,
        temp_dir=path()["temp_dir"],
        host=src()["host"],
        port=src()["port"],
        user=src()["user"],
        password=src()["password"],
        database=src()["database"],
    )
    os.system(bcp_string_src)
    # print(bcp_string_src)

    bcp_string_dst="""bcp "[ss].[{table_name}]" in "{temp_dir}/{schema_name}.{table_name}.dat" -S "{host},{port}" -U "{user}" -P "{password}" -d "{database}" -T -C RAW -n -E -a 10000""".format(
        schema_name=schema_name,
        table_name=table_name,
        sql=sql,
        temp_dir=path()["temp_dir"],
        host=dst()["host"],
        port=dst()["port"],
        user=dst()["user"],
        password=dst()["password"],
        database=dst()["database"],
    )
    os.system(bcp_string_dst)
    # os.remove("{temp_dir}/{schema_name}.{table_name}.dat".format(temp_dir=path()["temp_dir"]))
    # print (bcp_string_dst)

def data_flow():
    schema_name="dbo"
    table_name="telegram_messages"
    file_name="{temp_dir}/{schema_name}.{table_name}.dat".format(temp_dir=path()["temp_dir"],schema_name=schema_name,table_name=table_name)
    with open("{work_dir}/mssql2mssql/sql/src_select.sql".format(work_dir=path()["work_dir"]), 'r') as f: 
        sql = f.read()
    sql = sql.replace('<sfDate>', sfDate).replace('<sfUUID>', sfUUID)
    sql = sql.replace('\n','').replace('\r','').replace('\t','')
    # print(sql)
    bcp_string_src="""bcp "[{schema_name}].[{table_name}]" out "{temp_dir}/{schema_name}.{table_name}.dat" -S "{host},{port}" -U "{user}" -P "{password}" -d "{database}" -T -C RAW -n -E""".format(
        schema_name=schema_name,
        table_name=table_name,
        sql=sql,
        temp_dir=path()["temp_dir"],
        host=src()["host"],
        port=src()["port"],
        user=src()["user"],
        password=src()["password"],
        database=src()["database"],
    )
    try:
        os.remove(file_name)
    except:
        print("Error while deleting file ", file_name)
    os.system(bcp_string_src)
    # print(bcp_string_src)

    bcp_string_dst="""bcp "[ss].[{table_name}]" in "{temp_dir}/{schema_name}.{table_name}.dat" -S "{host},{port}" -U "{user}" -P "{password}" -d "{database}" -T -C RAW -n -E """.format(
        schema_name=schema_name,
        table_name=table_name,
        sql=sql,
        temp_dir=path()["temp_dir"],
        host=dst()["host"],
        port=dst()["port"],
        user=dst()["user"],
        password=dst()["password"],
        database=dst()["database"],
    )
    os.system(bcp_string_dst)
    try:
        os.remove(file_name)
    except:
        print("Error while deleting file ", file_name)
    # print (bcp_string_dst)

def create_ss():
    print("Create SS table started.")
    start = time.time()
    with open("{work_dir}/mssql2mssql/sql/create_ss.sql".format(work_dir=path()["work_dir"]), 'r') as f: 
            sql = f.read()
    conn = None
    try:
        conn = pymssql.connect(host=dst()["host"], database=dst()["database"], port=dst()["port"] ,user=dst()["user"], password=dst()["password"])
    except pymssql.InterfaceError:
        print("A MSSQLDriverException has been caught.")
        print(e)

    except (Exception, pymssql.DatabaseError) as e:
        print("A MSSQLDatabaseException has been caught.")
        print(e)

    # except (Exception, pymssql.DatabaseError) as error:
    #     print(error)
    finally:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
    print('Create SS table spent time: {} sec.'.format(round(time.time() - start, 2)))


def main():
    create_ss()
    data_flow()

if __name__ == "__main__":
    main()