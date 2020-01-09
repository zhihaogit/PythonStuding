-- Read Uncommitted是隔离级别最低的一种事务级别
-- 在这种隔离级别下，一个事务会读到另一个事务更新后但未提交的数据，如果另一个事务回滚，那么当前事务读到的数据就是脏数据，这就是脏数据(Dirty Read)

-- 分别开启两个 mysql客户端连接，按顺序依次执行事务 A和事务 B
-- 事务 A
-- step1
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
-- step2
BEGIN;
-- step3
UPDATE students SET name='Bob' WHERE id=1;
-- step4
-- step5
ROLLBACK;
-- step6
-- step7

-- 事务 B
-- step1
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
-- step2
BEGIN;
-- step3
-- step4
SELECT * FROM students WHERE id=1;
-- step5
-- step6
SELECT * FROM students WHERE id=1;
-- step7
COMMIT;

-- 当事务 A执行完第 3步时，它更新了 id=1的记录，但并未提交，而事务 B在第 4步读取到的数据就是未提交的数据
-- 随后，事务 A在第 5步进行了回滚，事务 B再次读取 id=1的记录，发现和上一次读取到的数据不一致，这就是脏读

-- 在 Read Uncommitted隔离级别下
-- 一个事务可能读取到另一个事务更新但未提交的数据，这个数据有可能是脏数据
