import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("SELECT AVG(marks) FROM students")
average = cursor.fetchone()[0]

if average is not None:
    print("Average marks:", round(average, 2))
else:
    print("No student records available.")

conn.close()