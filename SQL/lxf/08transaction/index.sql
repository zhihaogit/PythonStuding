-- 在执行 sql语句的时候，某些业务要求，一系列操作必须全部执行，而不能仅执行一部分

-- 从 id=1的账户给 id=2的账户转账 100元
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
-- 两条语句必须全部执行，第一条成功，第二条失败，就必须全部撤销
-- 这种把多条语句作为一个整体进行操作的功能，称为 数据库事务
-- 数据库事务可以确保该事务范围内的所有操作都可以全部成功或全部失败

-- 数据库事务具有 ACID这 4个特性：
-- A: Atomic，原子性
-- C: Consistent，一致性
-- I: Isolation，隔离性
-- D: Duration，持久性

-- 对于单条 sql语句，数据库系统自动将其作为一个事务执行，这种事务称为 隐式事务
-- 把多条 sql语句作为一个事务执行，使用 BEGIN开启一个事务，使用 COMMIT提交一个事务，这种事务称为 显式事务
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
-- COMMIT是指提交事务，即试图把事务内的所有 sql所做的修改永久保存，COMMIT语句执行失败，整个事务也会失败

BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
ROLLBACK;
-- ROLLBACK回滚事务，整个事务会失败


-- 隔离级别
-- 对于两个并发执行的事务，如果涉及到操作同一条记录，会带来数据的不一致性
-- 包括脏读，不可重复读，幻读等
-- 有针对性的选择数据库提供的隔离级别，避免数据不一致的问题
-- Isolation Level      脏读（Dirty Read）      不可重复读（Non Repeatable Read）      幻读（Phantom Read）
-- Read Uncommitted      Yes                     Yes                                 Yes
-- Read Committed        -                       Yes                                 Yes
-- Repeatable Read       -                       -                                   Yes
-- Serializable          -                       -                                   -