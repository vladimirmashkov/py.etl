from config import path as path
from config import s2 as src
from config import stage as stage
from config import dwh as dwh

import pg2pg.config as pkg

import time
import psycopg2
import uuid
# import pymssql
# import pandas as pd
# from sqlalchemy import create_engine

# from config import path as path
# from config import stage as dst

work_dir = path()["work_dir"]
host = stage()["host"]
database = stage()["database"]
port = stage()["port"]
user = stage()["user"]
password = stage()["password"]

package_name = pkg.package_name
sfPackageId = pkg.package_uuid


def sql_exec(sql, direction_type, name=""):
    start = time.time()
    connection = None
    if direction_type=='stage':
        connection = psycopg2.connect(
            host=stage()["host"], 
            port=stage()["port"], 
            database=stage()["database"], 
            user=stage()["user"], 
            password=stage()["password"]
            )
    if direction_type=='dwh':
        connection = psycopg2.connect(
            host=dwh()["host"], 
            port=dwh()["port"], 
            database=dwh()["database"], 
            user=dwh()["user"], 
            password=dwh()["password"]
            )
    if connection != None:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()
    if name!="":
        name = "{name}.sql ".format(name=name)
    print('sql execution - {name}in {direction_type} spent time: {time} sec.'.format(time=round(time.time() - start, 2),name=name, direction_type=direction_type))
    pass

def sql_file (name):
    file_name = "{work_dir}/{package_name}/sql/{name}.sql".format(work_dir=work_dir, package_name=package_name, name=name)
    return file_name

def open_file(file_name):
    with open(file_name, 'r') as f:
        prefix = "/* package_uuid: {package_uuid} */\n\r".format(package_uuid = pkg.package_uuid)
        content = f.read()
        content = prefix + content
        sql = content.replace('<null>sfPackageId</null>', '<null>{sfPackageId}</null>'.format(sfPackageId=sfPackageId))
    # print (sql)
    return sql

def chk_schema_stage():
    sql_exec(open_file(sql_file('chk_schema_stage')),'stage', 'chk_schema_stage')

def chk_schema_store():
    sql_exec(open_file(sql_file('chk_schema_store')),'dwh', 'chk_schema_store')

def chk_sd():
    sql_exec(open_file(sql_file('chk_sd')),'stage', 'chk_sd')

def chk_store():
    sql_exec(open_file(sql_file('chk_store')),'dwh', 'chk_store')

def crt_ss():
    sql_exec(open_file(sql_file('crt_ss')),'stage', 'crt_ss')
    sql_exec(open_file(sql_file('crt_ss')),'dwh', 'crt_ss')

def crt_temp():
    sql_exec(open_file(sql_file('crt_temp')),'stage', 'crt_temp')

def crt_temp_sd():
    sql_exec(open_file(sql_file('crt_temp_sd')),'stage', 'crt_temp_sd')

def crt_temp_store():
    sql_exec(open_file(sql_file('crt_temp_store')),'stage', 'crt_temp_store')
    sql_exec(open_file(sql_file('crt_temp_store')),'dwh', 'crt_temp_store')

def trf_temp():
    sql_exec(open_file(sql_file('trf_temp')),'stage', 'trf_temp')

def trf_temp_sd():
    sql_exec(open_file(sql_file('trf_temp_sd')),'stage', 'trf_temp_sd')

def trf_temp_store():
    sql_exec(open_file(sql_file('trf_temp_store')),'stage', 'trf_temp_store')

def trf_temp_store_dwh():
    sql_exec(open_file(sql_file('trf_temp_store_dwh')),'dwh', 'trf_temp_store_dwh')

def trf_store():
    sql_exec(open_file(sql_file('trf_store')),'dwh', 'trf_store')

def trn_clean_stage():
    sql_exec(open_file(sql_file('trn_clean_stage')),'stage', 'trn_clean_stage')

def trn_clean_store():
    sql_exec(open_file(sql_file('trn_clean_store')),'dwh', 'trn_clean_store')

def main():
    pass

if __name__ == "__main__":
    main()