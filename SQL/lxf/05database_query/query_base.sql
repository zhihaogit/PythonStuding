SELECT * from students;
-- select 是关键字，表示将要执行一个查询
-- * 表示所有列
-- FROM 表示将要从哪个表查询
-- 该 sql将查询出 students表中的所有数据
-- select查询的结果是一个二维表

SELECT 100 * 200;
-- select会直接计算出表达式的结果，可以用作计算，但不是sql的强项
-- 不带 from的 select语句有一个用途是判断当前的到数据库的连接是否有效

SELECT 1;
-- 测试数据库连接