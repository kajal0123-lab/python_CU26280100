import sqlite3

try:
    con = sqlite3.connect("school.db")
    print("New database created successfully!")
    con.close()
except sqlite3.Error as e:
    print("Error:", e)