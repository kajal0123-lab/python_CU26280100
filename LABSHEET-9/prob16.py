import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

roll = int(input("Enter roll number to delete: "))

cursor.execute(
    "DELETE FROM students WHERE roll_no = ?",
    (roll,)
)

conn.commit()

if cursor.rowcount > 0:
    print("Student record deleted successfully!")
else:
    print("Student not found.")

conn.close()