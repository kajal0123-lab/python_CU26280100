import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL
)
""")

# Add a course_id column to students if it does not exist.
columns = [
    row[1] for row in
    cursor.execute("PRAGMA table_info(students)").fetchall()
]

if "course_id" not in columns:
    cursor.execute(
        "ALTER TABLE students ADD COLUMN course_id INTEGER"
    )

courses = [
    (1, "Python"),
    (2, "Java"),
    (3, "Database Management")
]

cursor.executemany("""
INSERT OR IGNORE INTO courses (course_id, course_name)
VALUES (?, ?)
""", courses)

conn.commit()
print("Courses table created and data inserted successfully!")

conn.close()