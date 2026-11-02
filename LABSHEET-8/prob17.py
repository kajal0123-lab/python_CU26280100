import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

student_id = 1
new_name = "Aarav"

cur.execute(
    "UPDATE students SET name = ? WHERE id = ?",
    (new_name, student_id)
)

con.commit()

if cur.rowcount > 0:
    print("Student name updated successfully!")
else:
    print("Student not found.")

con.close()