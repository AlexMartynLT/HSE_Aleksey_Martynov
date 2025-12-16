-- 1. Группы
INSERT INTO student_groups (name) VALUES ('1 группа'), ('2 группа');

-- 2. Предметы
INSERT INTO subjects (name, type) VALUES 
('Математическая статистика', 'Math'),
('Математический анализ', 'Math'),
('Логика', 'Math'),
('Геометрия', 'Math'),
('Биология', 'Humanities'),
('Литература', 'Humanities'),
('Философия', 'Humanities'),
('Социология', 'Humanities');

-- 3. Преподаватели
INSERT INTO teachers (last_name, first_name, middle_name, email, phone) VALUES 
('Петров', 'Сергей', 'Павлович', 'petrov@nwu.edu', '89001112233'),
('Смирнова', 'Ирина', 'Сергеевна', 'smirnova@nwu.edu', '89004445566'),
('Павлов', 'Егор', 'Андреевич', 'pavlov@nwu.edu', '89007778899'),
('Фролов', 'Андрей', 'Петрович', 'frolov@nwu.edu', '89001234567'),
('Жаркова', 'Анна', 'Алексеевна', 'zharkova@nwu.edu', '89009876543');

-- 4. Нагрузка (2024 и 2025 годы)
INSERT INTO teacher_subjects (teacher_id, subject_id, academic_year) VALUES 
(1, 2, 2024), (1, 4, 2024), (1, 1, 2024), (1, 3, 2024), -- Петров 2024 (4 предмета)
(2, 5, 2024), (3, 6, 2024), (4, 7, 2024), (5, 8, 2024),
(1, 2, 2025), (1, 4, 2025), -- Петров 2025
(2, 5, 2025), (3, 6, 2025), (4, 7, 2025), (5, 8, 2025);

-- 5. Студенты
INSERT INTO students (last_name, first_name, group_id, birth_date, email) VALUES 
('Литвинов', 'Андрей', 1, '2003-05-15', 'litvinov@student.nwu.edu'),
('Смолов', 'Артем', 1, '2003-08-20', 'smolov@student.nwu.edu'),
('Котова', 'Екатерина', 1, '2004-01-10', 'kotova@student.nwu.edu'),
('Иванов', 'Александр', 2, '2003-11-05', 'ivanov@student.nwu.edu'),
('Швед', 'Илья', 2, '2003-03-30', 'shved@student.nwu.edu'),
('Яшин', 'Кирилл', 2, '2003-07-12', 'yashin@student.nwu.edu');

-- 6. Оценки (Выборочно для демонстрации)
-- 2024 год, 1 семестр (Экзамены)
INSERT INTO grades (student_id, subject_id, teacher_id, grade, grade_date, grade_type, semester) VALUES
(1, 2, 1, 5, '2024-01-15', 'Exam', 1), (3, 2, 1, 5, '2024-01-15', 'Exam', 1), -- Матан
(1, 5, 2, 3, '2024-01-20', 'Exam', 1), (3, 5, 2, 5, '2024-01-20', 'Exam', 1); -- Биология

-- 2024 год, 2 семестр
INSERT INTO grades (student_id, subject_id, teacher_id, grade, grade_date, grade_type, semester) VALUES
(1, 4, 1, 5, '2024-06-15', 'Exam', 2), (3, 4, 1, 5, '2024-06-15', 'Exam', 2), -- Геометрия
(1, 6, 3, 3, '2024-06-20', 'Exam', 2), (3, 6, 3, 5, '2024-06-20', 'Exam', 2); -- Литература

-- 2025 год, 3 семестр (Текущий)
INSERT INTO grades (student_id, subject_id, teacher_id, grade, grade_date, grade_type, semester) VALUES
(1, 3, 1, 5, '2025-01-15', 'Exam', 3), (3, 3, 1, 5, '2025-01-15', 'Exam', 3), -- Логика
(1, 7, 4, 2, '2025-01-20', 'Exam', 3), -- Литвинов 2
(2, 7, 4, 2, '2025-01-20', 'Exam', 3), -- Смолов 2
(3, 7, 4, 5, '2025-01-20', 'Exam', 3), -- Котова 5
(5, 7, 4, 2, '2025-01-20', 'Exam', 3), -- Швед 2
(6, 7, 4, 2, '2025-01-20', 'Exam', 3); -- Яшин 2

-- 2025 год, 4 семестр
INSERT INTO grades (student_id, subject_id, teacher_id, grade, grade_date, grade_type, semester) VALUES
(1, 1, 1, 5, '2025-06-15', 'Exam', 4), (3, 1, 1, 5, '2025-06-15', 'Exam', 4), -- Матстат
(1, 8, 5, 3, '2025-06-20', 'Exam', 4), (3, 8, 5, 5, '2025-06-20', 'Exam', 4); -- Социология