
DROP TABLE IF EXISTS Students;

CREATE TABLE Students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    birth_date DATE,
    email TEXT UNIQUE,
    course_name TEXT,
    enrollment_date DATE
);

INSERT INTO Students (name, birth_date, email, course_name, enrollment_date) VALUES
('Иван Иванов', '2000-01-15', 'ivan@example.com', 'Программирование', '2023-09-01'),
('Мария Петрова', '1999-03-22', 'maria@example.com', 'Математика', '2023-09-01'),
('Алексей Сидоров', '2001-07-10', 'alex@example.com', 'Программирование', '2023-09-01'),
('Елена Кузнецова', '2000-11-05', 'elena@example.com', 'Физика', '2023-09-01'),
('Дмитрий Смирнов', '1998-12-30', 'dmitry@example.com', 'Программирование', '2023-09-01');

SELECT name, email, course_name
FROM Students
WHERE course_name IN (
    SELECT DISTINCT course_name
    FROM Students
    WHERE course_name = 'Программирование'
);
