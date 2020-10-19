INSERT INTO "temp".s2_video_learningvideo
(	id, created_at, updated_at, uuid, url, "name", description, image, "number", duration_min, is_popular, 
	class_id, subject_id, access_id, sfdatetime, sfhash, sfpackageid, sfpackageflowid, sftableoid, sfxmin)
SELECT 	id, 
		to_timestamp(nullif(created_at,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>'), 'YYYY-MM-DD HH24:MI:SS.US') as created_at, 
		to_timestamp(nullif(updated_at,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>'), 'YYYY-MM-DD HH24:MI:SS.US')  as updated_at, 
		nullif (uuid,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::uuid as uuid, 
		nullif (url,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::varchar(500) as url,  
		nullif ("name",'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::varchar(100) as "name",  
		nullif (description,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::varchar(500) as description,  
		nullif ("image",'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>') as "image",  
		nullif ("number",'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::int4 as "number",  
		nullif (duration_min,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::int4  as duration_min,  
		nullif (is_popular,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::bool  as is_popular,  
		nullif (class_id,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::int4  as class_id,  
		nullif (subject_id,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::int4 as subject_id,
		nullif (access_id,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::int4  as access_id,  
		to_timestamp(nullif (sfdatetime,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>'), 'YYYY-MM-DD HH24:MI:SS.US')  as sfdatetime,  
		nullif (sfhash,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::uuid as sfhash,  
		nullif (sfpackageid,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::uuid as sfpackageid,  
		nullif (sfpackageflowid,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::uuid as sfpackageflowid,  
		nullif (sftableoid,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::int8  as sftableoid,  
		nullif (sfxmin,'<null>6ea92969-5561-4c26-9543-e4a8b20fd9b6</null>')::int8  as sfxmin 
FROM ss.s2_video_learningvideo;