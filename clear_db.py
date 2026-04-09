import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('University.db')
cursor = conn.cursor()

# Очистка таблиц от данных
cursor.execute("DELETE FROM Enrollments;")
cursor.execute("DELETE FROM Students;")
cursor.execute("DELETE FROM Courses;")

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()

print('Tables cleared successfully.')