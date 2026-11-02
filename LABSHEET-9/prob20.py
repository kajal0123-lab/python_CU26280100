import sqlite3

# Connect to database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    marks REAL
)
""")
conn.commit()


# Create: Add student
def add_student():
    roll = int(input("Enter roll number: "))
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    try:
        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?)",
            (roll, name, marks)
        )
        conn.commit()
        print("Student added successfully!")
    except sqlite3.IntegrityError:
        print("Roll number already exists.")


# Read: Display students
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if records:
        for record in records:
            print(record)
    else:
        print("No records found.")


# Update: Modify student
def update_student():
    roll = int(input("Enter roll number to update: "))
    name = input("Enter new name: ")
    marks = float(input("Enter new marks: "))

    cursor.execute("""
        UPDATE students
        SET name = ?, marks = ?
        WHERE roll = ?
    """, (name, marks, roll))

    conn.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student not found.")


# Delete: Remove student
def delete_student():
    roll = int(input("Enter roll number to delete: "))

    cursor.execute(
        "DELETE FROM students WHERE roll = ?",
        (roll,)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# Menu-driven program
while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter valid numeric values.")

conn.close()