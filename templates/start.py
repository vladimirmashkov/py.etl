from s1_video_learningVideo import sql as s1_video_learningVideo_sql
from s1_video_learningVideo import etl as s1_video_learningVideo_etl
# import s1_video_learningVideo as s1_video_learningVideo

def main():
    s1_video_learningVideo_sql.chk_schema_stage()
    s1_video_learningVideo_sql.chk_schema_store()
    s1_video_learningVideo_sql.crt_ss()
    s1_video_learningVideo_etl.to_stage()
    
    s1_video_learningVideo_sql.crt_temp()
    s1_video_learningVideo_sql.trf_temp()
    s1_video_learningVideo_sql.chk_sd()

    s1_video_learningVideo_sql.crt_temp_sd()
    s1_video_learningVideo_sql.trf_temp_sd()

    s1_video_learningVideo_sql.crt_temp_store()
    s1_video_learningVideo_sql.trf_temp_store()
    
    s1_video_learningVideo_etl.to_dwh()
    s1_video_learningVideo_sql.trf_temp_store_dwh()
    s1_video_learningVideo_sql.chk_store()
    s1_video_learningVideo_sql.trf_store()
    s1_video_learningVideo_sql.trn_clean_store()
    s1_video_learningVideo_sql.trn_clean_stage()
    
    pass

if __name__ == "__main__":
    main()