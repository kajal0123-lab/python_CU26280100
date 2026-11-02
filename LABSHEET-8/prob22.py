import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
SELECT students.name, students.marks, courses.course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.course_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()