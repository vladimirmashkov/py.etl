INSERT INTO "temp".s1_video_learningVideo
(	id, created_at, updated_at, uuid, url, "name", description, image, "number", duration_min, is_popular, 
	class_id, subject_id, access_id, sfDateTime, sfHash, sfPackageId, sfPackageFlowId, sfTableoId, sfXmin)
SELECT 	id, 
		to_timestamp(nullif(created_at,'<null>sfPackageId</null>'), 'YYYY-MM-DD HH24:MI:SS.US') as created_at, 
		to_timestamp(nullif(updated_at,'<null>sfPackageId</null>'), 'YYYY-MM-DD HH24:MI:SS.US')  as updated_at, 
		nullif (uuid,'<null>sfPackageId</null>')::uuid as uuid, 
		nullif (url,'<null>sfPackageId</null>')::varchar(500) as url,  
		nullif ("name",'<null>sfPackageId</null>')::varchar(100) as "name",  
		nullif (description,'<null>sfPackageId</null>')::varchar(500) as description,  
		nullif ("image",'<null>sfPackageId</null>') as "image",  
		nullif ("number",'<null>sfPackageId</null>')::int4 as "number",  
		nullif (duration_min,'<null>sfPackageId</null>')::int4  as duration_min,  
		nullif (is_popular,'<null>sfPackageId</null>')::bool  as is_popular,  
		nullif (class_id,'<null>sfPackageId</null>')::int4  as class_id,  
		nullif (subject_id,'<null>sfPackageId</null>')::int4 as subject_id,
		nullif (access_id,'<null>sfPackageId</null>')::int4  as access_id,  
		to_timestamp(nullif (sfDateTime,'<null>sfPackageId</null>'), 'YYYY-MM-DD HH24:MI:SS.US')  as sfDateTime,  
		nullif (sfHash,'<null>sfPackageId</null>')::uuid as sfHash,  
		nullif (sfPackageId,'<null>sfPackageId</null>')::uuid as sfPackageId,  
		nullif (sfPackageFlowId,'<null>sfPackageId</null>')::uuid as sfPackageFlowId,  
		nullif (sfTableoId,'<null>sfPackageId</null>')::int8  as sfTableoId,  
		nullif (sfXmin,'<null>sfPackageId</null>')::int8  as sfXmin 
FROM ss.s1_video_learningVideo;