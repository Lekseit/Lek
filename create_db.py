import sqlite3

# Подключение к базе данных (или создание, если не существует)
conn = sqlite3.connect('University.db')
cursor = conn.cursor()

# Создание таблицы Students
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT
);
''')

# Создание таблицы Courses
cursor.execute('''
CREATE TABLE IF NOT EXISTS Courses (
    CourseID INTEGER PRIMARY KEY,
    CourseName TEXT,
    Credits INTEGER
);
''')

# Создание таблицы Enrollments
cursor.execute('''
CREATE TABLE IF NOT EXISTS Enrollments (
    StudentID INTEGER,
    CourseID INTEGER,
    FOREIGN KEY(StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY(CourseID) REFERENCES Courses(CourseID)
);
''')

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()

print('Tables created successfully.')