
import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("PRAGMA table_info(students)")

print("ID | Name | Type | Not Null | Default | Primary Key")
for row in cur.fetchall():
    print(row)

con.close()