-- 外键
-- 可以把数据与另一张表关联起来，这种列称为 外键
-- 外键并不是通过列名实现的，而是通过定义外键约束实现的
ALTER TABLE students
ADD CONSTRAINT fk_class_id
-- 外键约束的名称 fk_class_id可以任意
FOREIGN KEY (class_id)
-- 指定了 class_id作为外键
REFERENCES classes (id);
-- 指定了这个外键将关联到 classes表的 id列（即 classes表的主键）
-- 通过定义外键约束，关系数据库可以保证无法插入无效的数据

-- 由于外键约束会降低数据库的性能，大部分互联网应用程序为了追求速度，并不设置外键约束，而是仅靠应用程序自身的逻辑正确

ALTER TABLE students
DROP FOREIGN KEY fk_class_id
-- 删除一个 外键约束，并没有删除外键这一列
-- 删除列是通过下面实现的
DROP COLUMN class_id


-- 多对多
-- 通过两个一对多关系实现，即通过一个中间表，关联两个一对多关系，就形成了多对多关系

-- 一对一
-- 一个表的记录对应到另一个表的唯一一个记录
-- 一些应用会把一个大表拆成两个一对一的表，目的是把经常读取和不经常读取的字段分开，以获得更高的性能