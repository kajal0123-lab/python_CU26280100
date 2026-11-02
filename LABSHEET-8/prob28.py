import sqlite3

try:
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    # Example query
    cursor.execute("SELECT * FROM unknown_table")

    print(cursor.fetchall())

except sqlite3.Error as e:
    print("Database error occurred:", e)

finally:
    if "conn" in locals():
        conn.close()