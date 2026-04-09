import sqlite3

# Подключение к базе данных (или создание, если не существует)
conn = sqlite3.connect('University.db')
cursor = conn.cursor()

# Создание таблицы Students с информацией о студентах и курсах
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    birth_date TEXT,
    email TEXT UNIQUE,
    course_name TEXT,
    enrollment_date TEXT
);
''')

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()

print('Таблица Students создана успешно.')