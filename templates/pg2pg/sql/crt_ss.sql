DROP TABLE IF EXISTS ss.S2_video_learningVideo CASCADE;
CREATE TABLE ss.S2_video_learningVideo (
	id int8 NULL, 
	created_at text NULL, 
	updated_at text NULL, 
	uuid text NULL, 
	url text NULL,
	name text NULL,
	description text NULL,
	image text NULL,
	"number" text NULL,
	duration_min text NULL, 
	is_popular text NULL,
	class_id text NULL,
	subject_id text NULL,
	access_id text NULL,
	sfDateTime text NULL, 
	sfHash text NULL,
	sfPackageId text NULL,
	sfPackageFlowId text NULL,
	sfTableoid text NULL, 
	sfXmin text NULL,
	CONSTRAINT PK_ss_S2_video_learningVideo PRIMARY KEY (id)
);