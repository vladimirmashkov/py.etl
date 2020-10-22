SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
    drop table if exists temp_store.s2_video_learningVideo cascade;
    drop table if exists ss.s2_video_learningVideo cascade;
COMMIT;