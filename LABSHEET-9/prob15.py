import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

roll = int(input("Enter roll number: "))
marks = float(input("Enter new marks: "))

cursor.execute("""
UPDATE students
SET marks = ?
WHERE roll_no = ?
""", (marks, roll))

conn.commit()

if cursor.rowcount > 0:
    print("Marks updated successfully!")
else:
    print("Student not found.")

conn.close()