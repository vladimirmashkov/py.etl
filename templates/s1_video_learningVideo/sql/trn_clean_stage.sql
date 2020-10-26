SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
    drop table if exists sd.s1_video_learningVideo cascade;
    ALTER TABLE if exists temp_sd.s1_video_learningVideo SET SCHEMA sd;
    drop table if exists ss.s1_video_learningVideo cascade;
    drop table if exists temp.s1_video_learningVideo cascade;
    drop table if exists temp_store.s1_video_learningVideo cascade;
COMMIT;