import sqlite3

def insert_student(student_id, name, age, marks):
    conn = sqlite3.connect("school.db")

    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO students (id, name, age, marks)
        VALUES (?, ?, ?, ?)
        """, (student_id, name, age, marks))

        conn.commit()
        print("Student inserted successfully!")

    except sqlite3.Error as e:
        conn.rollback()
        print("Error inserting student:", e)

    finally:
        conn.close()


def fetch_students():
    conn = sqlite3.connect("school.db")

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")

        for student in cursor.fetchall():
            print(student)

    except sqlite3.Error as e:
        print("Error fetching students:", e)

    finally:
        conn.close()


# Function calls
insert_student(10, "Anjali", 18, 91)
fetch_students()
