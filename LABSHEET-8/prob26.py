import sqlite3
import csv

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
records = cursor.fetchall()

column_names = [
    description[0] for description in cursor.description
]

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(column_names)
    writer.writerows(records)

print("Data exported to students.csv successfully!")

conn.close()
