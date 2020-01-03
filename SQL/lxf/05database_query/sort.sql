-- 排序
-- 查询结果集通常是按照 id排序的，也就是根据主键排序

SELECT id, name, gender, score FROM students ORDER BY score;
-- 根据成绩从低到高排序

SELECT id, name, gender, score FROM students ORDER BY score DESC;
-- DESC表示倒序，从高到低

SELECT id, name, gender, score FROM students ORDER BY score DESC, gender;
-- 先按 score列倒序，如果有相同的分数，再按 gender列排序

SELECT id, name, gender, score
FROM students
WHERE class_id = 1
ORDER BY score DESC;
-- 查询一班的学生成绩，并按倒序排列

SELECT * FROM students ORDER BY score;