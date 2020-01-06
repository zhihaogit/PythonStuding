-- update
-- 更新数据库表中的记录
-- UPDATE <表名> SET 字段1=值1, 字段2=值2, ...WHERE ...;

UPDATE
    students
SET
    name='大牛',
    score=66
WHERE
    id=1;
-- 更新 id为1这条记录中的 name和 score字段

UPDATE
    students
SET
    name='小牛',
    score=77
WHERE
    id>=5 AND id <=7;
-- 一次更新多条记录

UPDATE
    students
SET
    score=score+10
WHERE
    socre<80;
-- 更新字段使用表达式

UPDATE
    students
SET
    score=100
WHERE
    id=9999;
-- where条件匹配不到记录，update语句不会报错，也不会有记录被更新

UPDATE
    students
SET
    score=60;
-- students表的所有记录都会被更新
-- 危险操作


-- MYSQL
-- update语句会返回更新的行数以及 where条件匹配的行数
UPDATE
    students
SET
    name='大宝'
WHERE
    id=1;

