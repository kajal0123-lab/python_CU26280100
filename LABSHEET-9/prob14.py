import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

roll = int(input("Enter roll number to search: "))

cursor.execute(
    "SELECT * FROM students WHERE roll_no = ?",
    (roll,)
)

student = cursor.fetchone()

if student:
    print("Student found:", student)
else:
    print("Student not found.")

conn.close()