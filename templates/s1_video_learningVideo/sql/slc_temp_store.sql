SELECT 	id,
		COALESCE (TO_CHAR(created_at, 'YYYY-MM-DD HH24:MI:SS.US')::text,'<null>sfPackageId</null>') as created_at,
		COALESCE (TO_CHAR(updated_at, 'YYYY-MM-DD HH24:MI:SS.US')::text,'<null>sfPackageId</null>') as updated_at,
		COALESCE (uuid::text,'<null>sfPackageId</null>') as uuid,
		COALESCE (url::text,'<null>sfPackageId</null>') as url,
		COALESCE ("name"::text,'<null>sfPackageId</null>') as "name",
		COALESCE (description::text,'<null>sfPackageId</null>') as description,
		COALESCE (image::text,'<null>sfPackageId</null>') as image,
		COALESCE ("number"::text,'<null>sfPackageId</null>') as "number",
		COALESCE (duration_min::text,'<null>sfPackageId</null>') as duration_min,
		COALESCE (is_popular::text,'<null>sfPackageId</null>') as is_popular,
		COALESCE (class_id::text,'<null>sfPackageId</null>') as class_id,
		COALESCE (subject_id::text,'<null>sfPackageId</null>') as subject_id,
		COALESCE (access_id::text,'<null>sfPackageId</null>') as access_id,
		
		COALESCE (TO_CHAR(sfDateTime, 'YYYY-MM-DD HH24:MI:SS.US')::text,'<null>sfPackageId</null>') as sfDateTime,
		COALESCE (sfHash::text,'<null>sfPackageId</null>') as sfHash,
		COALESCE (sfPackageId::text,'<null>sfPackageId</null>') as sfPackageId,
		COALESCE (sfPackageFlowId::text,'<null>sfPackageId</null>') as sfPackageFlowId,
		COALESCE (sfTableoId::text,'<null>sfPackageId</null>') as sfTableoId,
		COALESCE (sfXmin::text,'<null>sfPackageId</null>') as sfXmin,
		COALESCE (TO_CHAR(sfFormerDateTime, 'YYYY-MM-DD HH24:MI:SS.US')::text,'<null>sfPackageId</null>') as sfFormerDateTime,
		sfChangeState
		
FROM temp_store.s1_video_learningVideo