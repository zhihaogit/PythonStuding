-- 实用 sql语句

-- 插入或替换
REPLACE INTO students (id, class_id, name, gender, score) VALUES (1, 1, '小明', 'F', 99);
-- 记录不存在，replace语句将插入新记录，存在的话就删除原有记录，再插入新记录

-- 插入或更新
INSERT INTO students (id, class_id, name, gender, score)
VALUES (1, 1, '小明', 'F', 99)
ON DUPLICATE
KEY UPDATE name='小明', gender='F', score=99;
-- 记录不存在，insert语句将插入新记录，存在的话，就更新该记录

-- 插入或忽略
INSERT INTO students (id, class_id, name, gender, score)
VALUES (1, 1, '小明', 'F', 99);
-- 记录不存在，insert语句将插入新记录，存在的话，就不做操作

-- 快照
-- 想要对一个表进行快照，即复制一份当前表的数据到一个新表，可以结合 CREATE TABLE和 SELECT
CREATE TABLE students_of_class1 SELECT * FROM students WHERE class_id=1;
-- 对 class_id=1的记录进行快照，并存储为新表 students_of_class1

-- 写入查询结果集
-- 结合 INSERT和 SELECT将 select语句的结果集直接插入到指定表中
CREATE TABLE statistics {
    id BIGINT NOT NULL AUTO_INCREMENT,
    class_id BIGINT NOT NULL,
    average DOUBLE NOT NULL,
    PRIMARY KEY (id)
};
-- 写入各班的平均成绩
INSERT INTO statistics (class_id, average)
SELECT class_id, AVG(score)
FROM students
GROUP BY class_id;

-- 强制使用指定索引
-- 数据库系统的查询优化器并不一定总是能使用最有索引
-- 可以使用 FORCE INDEX强制查询使用指定的索引
SELECT * FROM students FORCE INDEX (idx_class_id) WHERE class_id=1 ORDER BY id DESC;
-- 需要保证 idx_class_id必须存在