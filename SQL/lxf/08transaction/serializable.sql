-- Serializable是最严格的隔离级别
-- 所有事务按照次序依次执行
-- 因此脏读，不可重复读，幻读都不会出现
-- 由于事务是串行执行，所以效率会大大下降，应用程序的性能会急剧降低

-- 默认隔离级别
-- 如果没有指定隔离级别，数据库就会使用默认的隔离级别
-- 在 mysql中，使用 InnoDB，默认的隔离级别是 Repeatable Read