-- 连接查询
-- 连接查询对多个表进行 JOIN运算
-- 先确定一个主表作为结果集，然后把其他表的行有选择性地连接到主表结果集上

SELECT
 s.id,
 s.name,
 s.class_id,
 s.gender,
 s.score,
FROM
 students s;
-- 查询出 students表中的所有学生信息

-- 内连接
-- INNER JOIN只返回同时存在于两张表的行数据
 SELECT
  s.id,
  s.name,
  s.class_id,
  c.name class_name,
  s.gender,
  s.score
FROM
 students s
INNER JOIN
 classes c
ON
 s.class_id = c.id;
-- 结果集同时包含所在班级的名称
-- 1. 先确定主表，使用 FROM <表1>
-- 2. 在确定需要连接的表，使用 INNER JOIN <表2>
-- 3. 确定连接条件，使用 ON <条件...>
-- 4. 可选，WHERE语句，ORDER BY语句

-- 外连接
-- RIGHT OUTER JOIN返回右表都存在的行，左表不存在会补 NULL
-- LEFT OUTER JOIN返回左表否存在的行，右表不存在会补 NULL
-- FULL OUTER JOIN会把两张表的所有记录全部选择出来，并且自动把对方不存在的列填充为 NULL

SELECT
 s.id,
 s.name,
 s.class_id,
 c.name class_name,
 s.gender,
 s.score
FROM
 students s
RIGHT OUTER JOIN
 classes c
ON s.class_id = c.id;

INSERT INTO students
 (class_id, name, gender, score)
values
 (5, '新生', 'M', 88);

SELECT
 s.id,
 s.name,
 s.class_id,
 c.name class_name,
 s.gender,
 s.score
FROM
 students s
LEFT OUTER JOIN
 classes c
ON
 s.class_id = c.id;

-- mysql不支持 全外连接
SELECT
 s.id,
 s.name,
 s.class_id,
 c.name class_name,
 s.gender,
 s.score
FROM
 students s
FULL OUTER JOIN
 classes c
ON
 s.class_id = c.id;

-- JOIN查询需要先确定主表，然后把另一个表的数据附加到结果集上


