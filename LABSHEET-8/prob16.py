import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

student_id = 1
new_marks = 95

cur.execute(
    "UPDATE students SET marks = ? WHERE id = ?",
    (new_marks, student_id)
)

con.commit()

if cur.rowcount > 0:
    print("Marks updated successfully!")
else:
    print("Student not found.")

con.close()