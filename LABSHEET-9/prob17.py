import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM students")
total = cursor.fetchone()[0]

print("Total number of students:", total)

conn.close()