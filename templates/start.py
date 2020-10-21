from pg2pg import sql as pg2pg_sql
from pg2pg import etl as pg2pg_etl
# import pg2pg as pg2pg

def main():
    # pg2pg_sql.chk_schema_stage()
    # pg2pg_sql.chk_schema_store()
    # pg2pg_sql.crt_ss()
    # pg2pg_etl.to_stage()
    
    # pg2pg_sql.crt_temp()
    # pg2pg_sql.trf_temp()
    # pg2pg_sql.chk_sd()

    # pg2pg_sql.crt_temp_sd()
    # pg2pg_sql.trf_temp_sd()

    # pg2pg_sql.crt_temp_store()
    # pg2pg_sql.trf_temp_store()
    
    pg2pg_etl.to_dwh()



    # pg2pg_sql.chk_sd()
    # pg2pg_sql.chk_store()
    
    # pg2pg_sql.crt_temp()
    # pg2pg_sql.crt_temp_sd()
    # pg2pg_sql.crt_temp_store()
    # pg2pg_sql.trf_temp_sd()
    # pg2pg_sql.trf_temp_store()
    # pg2pg_sql.trn_clean_stage()
    # pg2pg_sql.trn_clean_store()





    pass

if __name__ == "__main__":
    main()