import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

table_name = "students"

cur.execute("""
SELECT name
FROM sqlite_master
WHERE type = 'table' AND name = ?
""", (table_name,))

if cur.fetchone():
    print("Table exists.")
else:
    print("Table does not exist.")

con.close()