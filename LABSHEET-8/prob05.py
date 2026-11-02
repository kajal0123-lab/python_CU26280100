import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("""
SELECT name
FROM sqlite_master
WHERE type = 'table'
ORDER BY name
""")

print("Tables in database:")
for row in cur.fetchall():
    print(row[0])

con.close()