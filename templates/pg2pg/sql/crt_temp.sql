DROP TABLE IF EXISTS "temp".S2_video_learningVideo CASCADE;
CREATE TABLE "temp".S2_video_learningVideo (
	id int8 NOT NULL,
	created_at timestamptz NULL,
	updated_at timestamptz NULL,
	uuid uuid NULL,
	url varchar(500) NULL,
	"name" varchar(100) NULL,
	description varchar(500) NULL,
	image text NULL,
	"number" int4 NULL,
	duration_min int4 NULL,
	is_popular bool NULL,
	class_id int4 NULL,
	subject_id int4 NULL,
	access_id int4 NULL,
	sfdatetime timestamptz null,
	sfhash uuid null,
	sfpackageid uuid null,
	sfpackageflowid uuid null,
	sftableoid int8 null,
	sfxmin int8 null,
    CONSTRAINT PK_temp_S2_video_learningVideo PRIMARY KEY (id)
);