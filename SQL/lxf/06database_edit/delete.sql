-- DELETE
-- 删除数据表中的记录
-- DELETE FROM <表名> WHERE ...;

DELETE FROM students WHERE id=1;
-- 删除 students表中 id=1的记录

DELETE FROM
    students
WHERE
    id>=5 AND id<=7;
-- 结合条件查询一次删除多条记录

DELETE FROM
    students
WHERE
    id=9999;
-- where语句没有匹配到任何记录，delete不会报错，也不会有任何记录被删除

DELETE FROM students;
-- 整个表的所有记录都会被删除
-- 危险操作

-- MYSQL
-- delete语句会返回删除的行数以及 where条件匹配到的行数