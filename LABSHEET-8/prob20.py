import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("DELETE FROM students")

con.commit()
print("All records deleted; table structure is unchanged.")

con.close()