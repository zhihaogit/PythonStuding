SELECT * FROM students;
-- 查询一张表的所有数据

SELECT * FROM students WHERE score >= 80;
-- 查询分数在 80即以上的数据

SELECT * FROM students WHERE score >= 80 AND gender = 'M';
-- 同时满足前后两个条件

SELECT * FROM students WHERE score >= 80 OR gender = 'M';
-- 满足两个条件的其中一个即可

SELECT * FROM students WHERE NOT class_id = 2;
-- 查找不符合该条件的记录
-- 等价于
SELECT * FROM students WHERE class_id<>2;

SELECT * FROM students WHERE (score < 80 OR score > 90) AND gender = 'M';
-- 按多个条件查询

-- 如果不加括号，条件运算按照 NOT, AND, OR的优先级进行
-- 括号改变优先级

-- 常用的条件表达式
--  使用 =判断相等                name='abc'          字符串需要用单引号包起来
--  使用 >判断大于                name>'abc'          字符串比较根据 ASCII码，中文字符按照数据库设置
--  使用 >=判断大于或相等          
--  使用 <判断小于
--  使用 <=判断小于或相等
--  使用 <>判断不相等
--  使用 LIKE判断相似             name LIKE 'ab%'     name LIKE '%bc%'    %表示任意字符，'ab%'将匹配 'ab','abc','abcd'

SELECT * FROM students WHERE score >= 60 and score <= 90;
SELECT * FROM students WHERE score BETWEEN 60 AND 90;
-- 取 score在 60-90范围的数据

-- 通过 WHERE条件查询，可以筛选出符合指定条件的记录，而不是整个表的所有记录