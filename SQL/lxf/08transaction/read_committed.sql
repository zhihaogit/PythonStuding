-- 在 read committed隔离级别下，一个事务可能遇到不可重复读（Non Repeatable Read）的问题
-- 不可重复读是指：
-- 在一个事务内，多次读同一数据，在这个事务还没结束时，如果另一个事务恰好修改了这个数据，那么在第一个事务中，两次读取的数据就可能不一致

-- 分别开启两个 mysql客户端连接，按顺序依次执行事务 A和事务 B
-- 事务 A
-- step1
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
-- step2
BEGIN;
-- step3
-- step4
UPDATE students SET name='Bob' WHERE id=1;
-- step5
COMMIT;
-- step6
-- step7

-- 事务 B
-- step1
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
-- step2
BEGIN;
-- step3
SELECT * FROM students WHERE id=1;
-- step4
-- step5
-- step6
SELECT * FROM students WHERE id=1;
-- step7
COMMIT;

-- 当事务 B第一次执行第 3步的查询时，得到的结果是 Alice
-- 随后由于事务 A在第 4步更新了这条记录并提交
-- 所以事务 B在第 6步再次执行同样的查询时，得到的结果变成了 Bob
-- 因此在 Read Committed隔离级别下，事务不可重复读同一条记录，因为很可能读到的结果不一致