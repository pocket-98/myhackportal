pragma foreign_keys=OFF;
begin TRANSACTION;

create table departments(
    id smallint primary key,
    dept varchar(4),
    dept_name varchar(64)
);

create table semesters(
    id smallint primary key,
    name varchar(16)
);

create table professors(
    id smallint primary key,
    name varchar(16)
);


create table courses(
    id smallint primary key,
    dept_id smallint,
    course_num varchar(8),
    course_name varchar(128),
    course_cred tinyint,
    course_reqs varchar(256),
    course_desc varchar(2048),
    course_attr varchar(256),
    semesters varchar(512)
);

create table sections(
    id int primary key,
    semester smallint,
    course_id smallint,
    prof_id smallint,
    section varchar(4),
    component varchar(8),
    days varchar(8),
    time varchar(16),
    loc varchar(64)
);

commit;

