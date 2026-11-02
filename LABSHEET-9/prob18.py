import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM students
ORDER BY name ASC
""")

records = cursor.fetchall()

for record in records:
    print(record)

conn.close()