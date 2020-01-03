-- 主键
-- 对于关系表，任意两条记录不能重复
-- 不能重复不是指两条记录不完全相同，而是指能够通过某个字段唯一区分出不同的记录，这个字段称为 主键

-- 记录一旦插入到表中，主键最好不要再修改，因为主键是用来唯一定位记录的
-- 不使用任何业务相关的字段作为主键

-- 常见的可作为 id字段的类型有
--  自增整数类型
--  全局唯一 GUID类型，GUID算法可以预算出主键

-- 使用 INT自增类型，一张表的记录数上限为 2147483647(约 21亿)
-- 使用 BIGINT自增类型，上限为 922亿亿条记录

-- 联合主键
-- 关系数据库还允许通过多个字段唯一标识记录，即两个或更多字段都设置为主键，这种主键称为联合主键
-- 联合主键，允许一列有重复，只要不是所有主键列都重复即可

-- 主键不应该允许为 NULL