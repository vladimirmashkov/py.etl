DROP TABLE IF EXISTS temp_store.s1_video_learningVideo CASCADE;
CREATE TABLE temp_store.s1_video_learningVideo (
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
	sfDateTime timestamptz null,
	sfHash uuid null,
	sfPackageId uuid null,
	sfPackageFlowId uuid null,
	sfTableoId int8 null,
	sfXmin int8 null,
	sfFormerDateTime timestamptz NULL,
    sfChangeState char(1) null,
    CONSTRAINT PK_temp_store_s1_video_learningVideo PRIMARY KEY (id)
);