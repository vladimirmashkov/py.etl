with _ss as (
        SELECT id, created_at, updated_at, uuid, url, "name", description, image, "number", duration_min, is_popular, class_id, subject_id, access_id, sfdatetime, sfhash, sfpackageid, sfpackageflowid, sftableoid, sfxmin
        FROM "temp".s2_video_learningvideo
),  _sd as (
        SELECT id, created_at, updated_at, uuid, url, "name", description, image, "number", duration_min, is_popular, class_id, subject_id, access_id, sfdatetime, sfhash, sfpackageid, sfpackageflowid, sftableoid, sfxmin
        FROM sd.s2_video_learningvideo
), _I as (
    select id from _ss
    except
    select id from _sd
), _Idt as (
    select _I.id, null::timestamptz as sfFormerDateTime
    from _I
    inner join _ss on _I.id = _ss.id
), _D as (
    select id from _sd
    except
    select id from _ss
), _Ddt as (
    select _D.id, _sd.sfDateTime as sfFormerDateTime
    from _D inner join _sd on _D.id = _sd.id
), _N as (
    select id, sfxmin
    from _sd
    intersect
    select id, sfxmin
    from _ss
), _Ndt as (
    select _N.id, _N.sfxmin, _sd.sfDateTime as sfFormerDateTime
    from _N inner join _sd on _N.id = _sd.id
), _U as (
    select _ss.id from _sd
    inner join _ss
    on  _sd.id = _ss.id
    and _sd.sfxmin <> _ss.sfxmin
), _Udt as (
    select _U.id, _sd.sfDateTime as sfFormerDateTime
    from _U inner join _sd on _U.id = _sd.id
), _IU as (
    select id, sfFormerDateTime, 'I'::char(1) as sfChangeState
    from _Idt
    union all
    select id, sfFormerDateTime, 'U'::char(1) as sfChangeState
    from _Udt
), _Dfull as (
    select _Ddt.id,
           created_at, updated_at, uuid, url, "name", description, image, "number", duration_min, is_popular, class_id, subject_id, access_id,
            (select sfdatetime from _ss where sfdatetime is not null limit 1) as sfDateTime,
           sfhash, sfpackageid, sfpackageflowid, sftableoid, sfxmin,
           _Ddt.sfFormerDateTime,
           'D'::char(1) as sfChangeState
    from _Ddt left join _ss on _Ddt.id = _ss.id
), _UIfull as (
    select _ss.*, _IU.sfFormerDateTime, _IU.sfChangeState from _IU
    inner join _ss
    on _IU.id = _ss.id
), _Nfull as (
    select _sd.*, _Ndt.sfFormerDateTime, 'N'::char(1) as sfChangeState
    from _Ndt inner join _sd on _Ndt.id = _sd.id
), _result as (
    select * from _Dfull
    union all
    select * from _Nfull
    union all
    select * from _UIfull
)
insert into temp_sd.s2_video_learningvideo
select * from _result
where sfChangeState not in ('D')
order by id;