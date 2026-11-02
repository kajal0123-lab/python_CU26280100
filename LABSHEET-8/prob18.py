import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

student_id = 3

cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
con.commit()

if cur.rowcount > 0:
    print("Student record deleted successfully!")
else:
    print("Student not found.")

con.close()