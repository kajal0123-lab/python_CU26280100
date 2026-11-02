import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("""
SELECT * FROM students
ORDER BY marks DESC
LIMIT 3
""")

print("Top 3 students:")
for row in cur.fetchall():
    print(row)

con.close()