import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM students
ORDER BY marks DESC
LIMIT 1
""")

student = cursor.fetchone()

if student:
    print("Student with highest marks:")
    print("Roll Number:", student[0])
    print("Name:", student[1])
    print("Marks:", student[2])
else:
    print("No student records found.")

conn.close()