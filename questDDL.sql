create database Assessment;

use Assessment;

create table quests
(
q_id int Primary key,
Label varchar(25),
quest varchar(120),
op_1 varchar(25),
op_2 varchar(25),
op_3 varchar(25),
op_4 varchar(25),
ans varchar(25)
);

select * from quests;

