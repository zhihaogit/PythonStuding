-- 多表查询
-- select查询不仅可以从一张表查询数据，还可以从多张表同时查询数据
-- SELECT * FROM <表1> <表2>

SELECT * FROM students, classes;
-- 同时查询 students和 classes表
-- 查询的结果也是一个二维表，它是两个表的乘积
-- 结果集的列数是 两张表的列数之后，行数是两表的行数之积
-- 这种多表查询称为 笛卡尔查询

SELECT
 students.id sid,
 students.name,
 students.gender,
 students.score,
 classes.id cid,
 classes.name cname
FROM students, classes;
-- 为结果集中重名的 id起别名
-- 多表查询时，使用 表名.列名的方式来引用列和设置别名，避免了结果集的列名重复问题

SELECT
 s.id sid,
 s.name,
 s.gender,
 s.score,
 c.id cid,
 c.name cname
FROM
 students s,
 classes c;
-- 允许给表设置一个别名，简化一下引用

 SELECT
  s.id sid,
  s.name,
  s.gender,
  s.score,
  c.id cid,
  c.name cname
FROM
 students s,
 classes c
WHERE
 s.gender = 'M' AND
 c.id = 1;
-- 结合条件查询进行多表查询