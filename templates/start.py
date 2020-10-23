from s2_video_learningVideo import sql as s2_video_learningVideo_sql
from s2_video_learningVideo import etl as s2_video_learningVideo_etl
# import s2_video_learningVideo as s2_video_learningVideo

def main():
    s2_video_learningVideo_sql.chk_schema_stage()
    s2_video_learningVideo_sql.chk_schema_store()
    s2_video_learningVideo_sql.crt_ss()
    s2_video_learningVideo_etl.to_stage()
    
    s2_video_learningVideo_sql.crt_temp()
    s2_video_learningVideo_sql.trf_temp()
    s2_video_learningVideo_sql.chk_sd()

    s2_video_learningVideo_sql.crt_temp_sd()
    s2_video_learningVideo_sql.trf_temp_sd()

    s2_video_learningVideo_sql.crt_temp_store()
    s2_video_learningVideo_sql.trf_temp_store()
    
    s2_video_learningVideo_etl.to_dwh()
    s2_video_learningVideo_sql.trf_temp_store_dwh()
    s2_video_learningVideo_sql.chk_store()
    s2_video_learningVideo_sql.trf_store()
    s2_video_learningVideo_sql.trn_clean_store()
    s2_video_learningVideo_sql.trn_clean_stage()
    
    pass

if __name__ == "__main__":
    main()