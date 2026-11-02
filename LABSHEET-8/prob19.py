import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("DELETE FROM students WHERE marks < ?", (40,))
deleted = cur.rowcount

con.commit()

print("Number of students deleted:", deleted)

con.close()