import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute(
    "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
    (1, "Aman", 18, 85)
)

con.commit()
print("Record inserted successfully!")
con.close()