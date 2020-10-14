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