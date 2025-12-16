-- === ЧАСТЬ 1: АНАЛИТИЧЕСКИЕ ЗАПРОСЫ ===
-- 1. Студенты по предмету 'Математический анализ'
SELECT DISTINCT s.last_name, s.first_name, sub.name AS subject
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = 'Математический анализ';
-- 2. Предметы преподавателя Петрова
SELECT DISTINCT t.last_name, sub.name AS subject
FROM teachers t
JOIN teacher_subjects ts ON t.id = ts.teacher_id
JOIN subjects sub ON ts.subject_id = sub.id
WHERE t.last_name = 'Петров';
-- 3. Средний балл студента Литвинова по всем предметам
SELECT s.last_name, AVG(g.grade) AS total_average
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.last_name = 'Литвинов';
-- 4. Рейтинг преподавателей по средней оценке студентов
SELECT t.last_name, AVG(g.grade) AS avg_rating
FROM teachers t
JOIN grades g ON t.id = g.teacher_id
GROUP BY t.id
ORDER BY avg_rating DESC;
-- 5. Преподаватели, которые вели > 3 предметов в 2024 году
SELECT t.last_name, COUNT(ts.subject_id) AS subjects_count_2024
FROM teachers t
JOIN teacher_subjects ts ON t.id = ts.teacher_id
WHERE ts.academic_year = 2024
GROUP BY t.id
HAVING subjects_count_2024 > 3;
-- 6. Студенты: средний балл мат > 4, гум < 3
SELECT s.last_name
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
GROUP BY s.id
HAVING
AVG(CASE WHEN sub.type = 'Math' THEN g.grade END) > 4
AND
AVG(CASE WHEN sub.type = 'Humanities' THEN g.grade END) < 3;
-- 7. Предмет с наибольшим кол-вом двоек в текущем семестре (3 сем, 2025)
SELECT sub.name, COUNT(g.id) as count_of_twos
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
WHERE g.grade = 2 AND g.semester = 3 AND YEAR(g.grade_date) = 2025
GROUP BY sub.id
ORDER BY count_of_twos DESC
LIMIT 1;
-- 8. Отличники по всем экзаменам и их преподаватели
SELECT s.last_name, GROUP_CONCAT(DISTINCT t.last_name SEPARATOR ', ') as teachers
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN teachers t ON g.teacher_id = t.id
WHERE g.grade_type = 'Exam'
GROUP BY s.id
HAVING MIN(g.grade) = 5;
-- 9. Динамика среднего балла студента Литвинова по годам
SELECT YEAR(g.grade_date) as year, AVG(g.grade) as avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.last_name = 'Литвинов'
GROUP BY YEAR(g.grade_date)
ORDER BY year;
-- 10. Группы с лучшим баллом по Матанализу
SELECT sg.name, AVG(g.grade) as group_avg
FROM student_groups sg
JOIN students s ON sg.id = s.group_id
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = 'Математический анализ'
GROUP BY sg.id
ORDER BY group_avg DESC;
-- === ЧАСТЬ 2: МОДИФИКАЦИЯ ДАННЫХ ===
-- 1. Вставка студента
INSERT INTO students (last_name, first_name, group_id, birth_date, email, phone)
VALUES ('Соколов', 'Дмитрий', 1, '2004-05-20', 'sokolov@nwu.edu', '89990000001');
-- 2. Обновление контактов преподавателя по ФИО (берем полностью, т.к.
-- фамилия может совпадать
UPDATE teachers
SET email = 'new_smirnova_email@nwu.edu'
WHERE last_name = 'Смирнова' AND first_name = 'Ирина' AND middle_name = 'Сергеевна';
-- 3. Мягкое удаление предмета (Архивация)
UPDATE subjects SET is_active = FALSE WHERE name = 'Социология';
-- Попытка вставки оценки по архивному предмету (Вызовет ошибку Триггера)
-- INSERT INTO grades ... VALUES ... (см. отчет, сам триггер - п. 8 в файле structure.sql)
-- 4. Вставка новой записи об оценке
-- Поставим оценку 4 новому студенту Соколову по предмету "Логика" у преподавателя Петрова.
-- Используем подзапросы, чтобы найти ID по фамилиям.
INSERT INTO grades (student_id, subject_id, teacher_id, grade, grade_date, grade_type, semester)
VALUES (
(SELECT id FROM students WHERE last_name = 'Соколов' LIMIT 1), -- Ищем ID студента
(SELECT id FROM subjects WHERE name = 'Логика' LIMIT 1),       -- Ищем ID предмета
(SELECT id FROM teachers WHERE last_name = 'Петров' LIMIT 1),  -- Ищем ID преподавателя
4,           -- Оценка
CURDATE(),   -- Дата (сегодня)
'Regular',   -- Тип оценки
4            -- Семестр
);
