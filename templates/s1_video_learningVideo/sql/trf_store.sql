INSERT INTO store.s1_video_learningVideo (
		id, created_at, updated_at, uuid, url, "name", description, image, "number", duration_min, is_popular, class_id, subject_id, access_id, 
		sfDateTime, sfHash, sfPackageId, sfPackageFlowId, sfTableoId, sfXmin, sfFormerDateTime, sfChangeState)
select	id, created_at, updated_at, uuid, url, "name", description, image, "number", duration_min, is_popular, class_id, subject_id, access_id, 
		sfDateTime, sfHash, sfPackageId, sfPackageFlowId, sfTableoId, sfXmin, sfFormerDateTime, sfChangeState
FROM temp_store.s1_video_learningVideo
ORDER BY sfChangeState, id;