import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("SELECT name, marks FROM students")

for row in cur.fetchall():
    print("Name:", row[0], "| Marks:", row[1])

con.close()