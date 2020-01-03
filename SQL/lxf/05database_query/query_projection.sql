-- 投影查询
-- 让查询的结果集仅包含指定列
SELECT id, score, name FROM students;
-- 结果集的列的顺序和原表可以不一样，因为只返回了指定的列

SELECT id, score points, name FROM students;
-- 将 score起一个别名 points，作用于查询结果集

SELECT id, score points, name FROM students WHERE gender = 'M';
-- 使用 where实现条件查询
