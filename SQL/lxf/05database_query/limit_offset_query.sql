-- 分页查询
-- 实际是从结果集中截取出第 m-n条记录
-- LIMIT <M> OFFSET <N>

SELECT id, name, gender, score FROM students ORDER BY score DESC;

SELECT id, name, gender, score
FROM students
ORDER BY score DESC
LIMIT 3 OFFSET 0;
-- 查询第一页

-- SQL记录集的索引从 0开始

SELECT id, name, gender, score
FROM students
ORDER BY score DESC
LIMIT 3 OFFSET 3;
-- 查询第二页

SELECT id, name, gender, score
FROM students
ORDER BY score DESC
LIMIT 3 OFFSET 6;
-- 查询第三页

SELECT id, name, gender, score
FROM students
ORDER BY score DESC
LIMIT 3 OFFSET 9;
-- 查询第四页

-- OFFSET超过 原本记录集的数量，将得到一个空的结果集
SELECT id, name, gender, score
FROM students
ORDER BY score DESC
LIMIT 3 OFFSET 100;

-- OFFSET是可选的，默认从索引 0开始
LIMIT 15 OFFSET 30
-- 简写成
LIMIT 30, 15

-- 获取总条数
SELECT COUNT(*) FROM students;