-- 1. Создание базы данных
CREATE DATABASE new_west_uni;
USE new_west_uni;

-- 2. Таблица групп
CREATE TABLE student_groups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- 3. Таблица преподавателей
CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    birth_date DATE,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20)
);

-- 4. Таблица студентов
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    birth_date DATE NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES student_groups(id) ON DELETE SET NULL
);

-- 5. Таблица предметов
-- is_active: флаг для "мягкого удаления" (архивации)
CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    type ENUM('Humanities', 'Math') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- 6. Связь преподавателей и предметов
-- academic_year: позволяет хранить историю преподавания по годам
CREATE TABLE teacher_subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_id INT NOT NULL,
    subject_id INT NOT NULL,
    academic_year INT NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);

-- 7. Таблица оценок
-- grade_type: разделяет экзамены и текущие оценки
CREATE TABLE grades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    teacher_id INT NOT NULL,
    grade INT NOT NULL CHECK (grade >= 1 AND grade <= 5),
    grade_date DATE NOT NULL,
    grade_type ENUM('Regular', 'Exam') NOT NULL DEFAULT 'Regular',
    semester INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id) ON DELETE CASCADE
);

-- 8. Триггер: Запрет на выставление оценок по архивным предметам
DELIMITER //
CREATE TRIGGER prevent_grade_for_inactive_subject
BEFORE INSERT ON grades
FOR EACH ROW
BEGIN
    DECLARE subject_status BOOLEAN;
    SELECT is_active INTO subject_status FROM subjects WHERE id = NEW.subject_id;
    IF subject_status = FALSE THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'ОШИБКА: Нельзя выставить оценку по архивному предмету!';
    END IF;
END;
//
DELIMITER ;