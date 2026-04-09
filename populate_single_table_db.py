import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('University.db')
cursor = conn.cursor()

# Добавление данных о студентах и их курсах
students_data = [
    ('Иван Иванов', '2000-01-15', 'ivan@example.com', 'Программирование', '2023-09-01'),
    ('Мария Петрова', '1999-03-22', 'maria@example.com', 'Математика', '2023-09-01'),
    ('Алексей Сидоров', '2001-07-10', 'alex@example.com', 'Программирование', '2023-09-01'),
    ('Елена Кузнецова', '2000-11-05', 'elena@example.com', 'Физика', '2023-09-01'),
    ('Дмитрий Смирнов', '1998-12-30', 'dmitry@example.com', 'Программирование', '2023-09-01')
]

# Вставка данных
cursor.executemany("INSERT INTO Students (name, birth_date, email, course_name, enrollment_date) VALUES (?, ?, ?, ?, ?)", students_data)

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()

print('Данные о студентах добавлены успешно.')