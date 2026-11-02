import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("SELECT COUNT(*) FROM students")
count = cur.fetchone()[0]

print("Total number of students:", count)

con.close()