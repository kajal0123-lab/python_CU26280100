import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

roll = int(input("Enter roll number: "))
name = input("Enter student name: ")
marks = float(input("Enter marks: "))

cursor.execute("""
INSERT INTO students (roll_no, name, marks)
VALUES (?, ?, ?)
""", (roll, name, marks))

conn.commit()

print("Student record inserted successfully!")

conn.close()