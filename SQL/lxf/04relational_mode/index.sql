-- 索引
-- 有很多条记录时，为了获得非常快的查找速度，需要使用索引
-- 索引是关系数据库中对某一列或多个列的值进行预排序的数据结构
-- 通过索引，数据库系统不必扫描整个表，而是直接定位到符合条件的记录，加快了查询速度

ALTER TABLE students
ADD INDEX idx_score (score);
-- 对 score列创建索引

ALTER TABLE students
ADD INDEX idx_name_score (name, score);
-- 创建多列索引

-- 索引的效率取决于索引列的值是否散列，即该列的值重复性越低，索引效率越高
-- 可以对一张表创建多个索引
-- 索引的优点是提高了查询效率，缺点是在插入、更新和删除记录时，需要同时修改索引

-- 唯一索引
ALTER TABLE students
ADD CONSTRAINT uni_name UNIQUE (name);
-- 通过创建唯一索引，可以保证某一列的值具有唯一性
-- 数据库索引对于用户和应用程序都是透明的