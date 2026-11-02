import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

students = [
    (2, "Priya", 19, 92),
    (3, "Rahul", 18, 76),
    (4, "Neha", 20, 88),
    (5, "Rohit", 19, 35)
]

cur.executemany(
    "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
    students
)

con.commit()
print("Multiple records inserted successfully!")