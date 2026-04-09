import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('University.db')
cursor = conn.cursor()

# Использование вложенного запроса для поиска студентов, записанных на курс по программированию
# В данном случае вложенный запрос не обязателен, так как можно обойтись простым WHERE,
# но для демонстрации используем подзапрос
cursor.execute('''
SELECT name, email, course_name
FROM Students
WHERE course_name IN (SELECT DISTINCT course_name FROM Students WHERE course_name = 'Программирование');
''')

# Получение и вывод результатов
results = cursor.fetchall()
print("Студенты, записанные на курс по программированию:")
for row in results:
    print(f"Имя: {row[0]}, Email: {row[1]}, Курс: {row[2]}")

# Закрытие подключения
conn.close()