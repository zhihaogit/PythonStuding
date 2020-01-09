-- 在 Repeatable Read隔离级别下，一个事务可能会遇到幻读（Phantom Read）的问题
-- 幻读是指，在一个事务中，第一次查询某条记录，发现没有，但是，当试图更新这条不存在的记录时，竟然能成功，并且再次读取同一记录，就出现了

-- 分别开启两个MySQL客户端连接，按顺序依次执行事务A和事务B
-- 事务 A
-- step1
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
-- step2
BEGIN;
-- step3
-- step4
INSERT INTO students (id, name) VALUES (99, 'Bob');
-- step5
COMMIT;
-- step6
-- step7
-- step8
-- step9

-- 事务 B
-- step1
SET TRANSACTION ISOLATION LEVEL PEPEATABLE READ;
-- step2
BEGIN;
-- step3
SELECT * FROM students WHERE id=99;
-- step4
-- step5
-- step6
SELECT * FROM students WHERE id=99;
-- step7
UPDATE students SET name='Alice' WHERE id=99;
-- step8
SELECT * FROM students WHERE id=99;
-- step9
COMMIT;

-- 事务B在第3步第一次读取id=99的记录时，读到的记录为空，说明不存在id=99的记录
-- 随后，事务A在第4步插入了一条id=99的记录并提交。事务B在第6步再次读取id=99的记录时，读到的记录仍然为空
-- 但是，事务B在第7步试图更新这条不存在的记录时，竟然成功了，并且，事务B在第8步再次读取id=99的记录时，记录出现了

-- 幻读就是没有读到的记录，以为不存在，但其实是可以更新成功的，并且，更新成功后，再次读取，就出现了