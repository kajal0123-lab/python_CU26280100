import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
records = cursor.fetchall()

if records:
    for record in records:
        print(record)
else:
    print("No student records found.")

conn.close()