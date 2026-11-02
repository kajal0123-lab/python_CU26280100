
import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks REAL
)
""")

con.commit()
print("Students table created successfully!")
con.close()