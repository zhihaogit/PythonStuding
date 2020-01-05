-- 聚合查询
-- 对于统计总数、平均数这类计算，sql提供了专门的聚合函数，使用聚合函数进行查询，就是聚合查询，可以快速获得结果

SELECT COUNT(*) FROM students;
-- 查询 students表一共个有多少记录

SELECT COUNT(*) num FROM students;
-- 聚合查询之后，给列名设置一个别名

SELECT COUNT(*) boys FROM students WHERE gender = 'M';
-- 结合 where条件查询

SELECT SUM(score) sum FROM students;
-- sum计算某一列的合计值，该列必须为数值类型

SELECT AVG(score) average FROM students;
-- avg计算某一列的平均值，该列必须为数值类型

SELECT MAX(score) max FROM students;
-- max计算某一列的最大值

SELECT MIN(score) min FROM students;
-- min计算某一列的最小值

-- max, min不仅限于数值类型
-- 如果是字符类型，会返回排序最后和排序最前的字符

SELECT AVG(score) average FROM students WHERE gender = 'M';
-- 使用聚合查询计算男生平均成绩

SELECT AVG(score) average FROM students WHERE gender = 'X';
-- 聚合查询的 where条件没有匹配到任何行
-- count会返回 0
-- sum, avg, max, min会返回 NULL

SELECT CEILING(COUNT(*) / 3) FROM students;
-- 每页 3条记录，通过聚合查询获得总页数


-- 分组
-- 分组聚合

SELECT COUNT(*) num FROM students GROUP BY class_id;
-- 会按 class_id先聚合，再分别计算

SELECT name, class_id, COUNT(*) num FROM students GROUP BY class_id;
-- 在任意分组中，只有 class_id都相同，name是不同的，sql引擎不能把多个 name的值放一行记录中
-- 聚合查询的列中，只能放入分组的列

SELECT class_id, gender, COUNT(*) num FROM students GROUP BY class_id, gender;
-- 结果集的数据分别对应各班级的男生和女生的人数

SELECT class_id, AVG(score) average FROM students GROUP BY class_id;
-- 查询每个班级的平均分

SELECT class_id, gender, AVG(score) FROM students GROUP BY class_id, gender;
-- 查询每个班级中男女的平均分
