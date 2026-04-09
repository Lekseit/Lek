import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('University.db')
cursor = conn.cursor()

# Выполнение запроса на получение списка студентов и курсов
cursor.execute('''
SELECT Students.FirstName, Students.LastName, Courses.CourseName
FROM Students
JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
JOIN Courses ON Enrollments.CourseID = Courses.CourseID;
''')

# Получение и вывод результатов
results = cursor.fetchall()
for row in results:
    print(f"{row[0]} {row[1]} - {row[2]}")

# Закрытие подключения
conn.close()