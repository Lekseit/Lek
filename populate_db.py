import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('University.db')
cursor = conn.cursor()

# Добавление данных в таблицу Students
cursor.execute("INSERT INTO Students (FirstName, LastName) VALUES ('Иван', 'Иванов')")
cursor.execute("INSERT INTO Students (FirstName, LastName) VALUES ('Мария', 'Петрова')")
cursor.execute("INSERT INTO Students (FirstName, LastName) VALUES ('Алексей', 'Сидоров')")

# Добавление данных в таблицу Courses
cursor.execute("INSERT INTO Courses (CourseName, Credits) VALUES ('Математика', 4)")
cursor.execute("INSERT INTO Courses (CourseName, Credits) VALUES ('Физика', 3)")
cursor.execute("INSERT INTO Courses (CourseName, Credits) VALUES ('Программирование', 5)")

# Добавление данных в таблицу Enrollments
cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (1, 1)")  # Иван -> Математика
cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (1, 3)")  # Иван -> Программирование
cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (2, 2)")  # Мария -> Физика
cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (3, 1)")  # Алексей -> Математика
cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (3, 2)")  # Алексей -> Физика
cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (3, 3)")  # Алексей -> Программирование

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()

print('Data inserted successfully.')