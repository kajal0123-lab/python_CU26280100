import sqlite3

DB_NAME = "school.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        marks REAL
    )
    """)

    conn.commit()
    conn.close()


def add_student():
    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        marks = float(input("Enter student marks: "))

        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("""
            INSERT INTO students (id, name, age, marks)
            VALUES (?, ?, ?, ?)
            """, (student_id, name, age, marks))

        print("Student added successfully!")

    except (ValueError, sqlite3.Error) as e:
        print("Error:", e)


def view_students():
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.execute("SELECT * FROM students")
            records = cursor.fetchall()

        if records:
            print("\nID | Name | Age | Marks")
            print("-" * 30)

            for student in records:
                print(
                    student[0], "|",
                    student[1], "|",
                    student[2], "|",
                    student[3]
                )
        else:
            print("No student records found.")

    except sqlite3.Error as e:
        print("Error:", e)


def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))
        new_marks = float(input("Enter new marks: "))

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.execute("""
            UPDATE students
            SET marks = ?
            WHERE id = ?
            """, (new_marks, student_id))

        if cursor.rowcount > 0:
            print("Student marks updated successfully!")
        else:
            print("Student ID not found.")

    except (ValueError, sqlite3.Error) as e:
        print("Error:", e)


def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.execute(
                "DELETE FROM students WHERE id = ?",
                (student_id,)
            )

        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student ID not found.")

    except (ValueError, sqlite3.Error) as e:
        print("Error:", e)


def main():
    create_table()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Marks")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Exiting Student Management System.")
            break

        else:
            print("Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main()