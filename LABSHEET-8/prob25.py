import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
SELECT age, COUNT(*)
FROM students
GROUP BY age
ORDER BY age
""")

for row in cursor.fetchall():
    print("Age:", row[0], "| Number of students:", row[1])

conn.close()