import sqlite3
import csv

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
            INSERT INTO students (id, name, age, marks)
            VALUES (?, ?, ?, ?)
            """, (
                int(row["id"]),
                row["name"],
                int(row["age"]),
                float(row["marks"])
            ))

    conn.commit()
    print("CSV data imported successfully!")

except (sqlite3.Error, OSError, ValueError, KeyError) as e:
    conn.rollback()
    print("Import failed:", e)

finally:
    conn.close()