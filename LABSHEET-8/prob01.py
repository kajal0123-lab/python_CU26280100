import sqlite3

try:
    con = sqlite3.connect("school.db")
    print("Database connected successfully!")
    con.close()
except sqlite3.Error as e:
    print("Database error:", e)