import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS students")

con.commit()
print("Students table dropped successfully!")
con.close()