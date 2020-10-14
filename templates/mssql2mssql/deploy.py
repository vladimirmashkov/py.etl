import psycopg2
from config import config_eds_group
import time

def file_list():
    file_list = [
        'config.create_schema.sql',
        # 'terminate_other_connections.sql',
        '_create_types.sql', 
        'ss.lesson.sql',
        'etl.fill-up_SsLesson.sql',
        'sd.lesson.sql',
        'temp.lesson.sql',
        'etl.fill-up_TempLesson.sql',
        'temp_sd.lesson.sql',
        'etl.fill-up_TempSdLesson.sql',
        'temp_store.lesson.sql',
        'etl.fill-up_TempStoreLesson.sql',
        'store.lesson.sql',
        'etl.inreach_StoreLesson.sql',
        'ss.student_education_group.sql',
        'etl.fill-up_SsStudent_education_group.sql',
        'sd.student_education_group.sql',
        'temp.student_education_group.sql',
        'etl.fill-up_TempStudent_education_group.sql',
        'temp_sd.Student_education_group.sql',
        'etl.fill-up_TempSdStudent_education_group.sql',
        'temp_store.Student_education_group.sql',
        'etl.fill-up_TempStoreStudent_education_group.sql',
        'store.Student_education_group.sql',
        'etl.inreach_StoreStudent_education_group.sql',
        ]
    return file_list

def pg_connection(file_name):
    conn = None
    try:
        params = config_eds_group()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql_file = open(file_name,'r')
        cur.execute(sql_file.read())
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def main ():
    for file_name in file_list():
        print(file_name)
        pg_connection (file_name)
        # time.sleep(5)

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config_eds_group()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    main()
    # connect()