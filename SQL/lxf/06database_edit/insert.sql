-- 向数据库表中插入一条新记录时，需要使用 INSERT语句
-- 基本语法 INSERT INTO <表名> (字段1, 字段2, ...) VALUES (值1, 值2, ...);

INSERT INTO
    students
    (class_id, name, gender, score)
VALUES
    (2, '大牛', 'M', 80);
-- 新增一条记录

-- 字段顺序不必和数据库表的字段顺序一致
-- 但值的顺序必须和字段顺序一致
-- 还可以一次性添加多条记录，只需要在 VALUES子句中指定多个记录，每个记录是由 (...)包含的一组值

INSERT INTO
    students
    (class_id, name, gender, score)
VALUES
    (1, '大宝', 'M', 87),
    (2, '二宝', 'M', 81);
-- 一次性插入两条数据