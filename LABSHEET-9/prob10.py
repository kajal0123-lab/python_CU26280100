FILE_NAME = "students.txt"


def read_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")
                students.append({
                    "roll": int(roll),
                    "name": name,
                    "marks": float(marks)
                })
    except FileNotFoundError:
        pass

    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(
                f'{s["roll"]},{s["name"]},{s["marks"]}\n'
            )


def add_student():
    students = read_students()
    roll = int(input("Enter roll number: "))

    if any(s["roll"] == roll for s in students):
        print("Roll number already exists.")
        return

    name = input("Enter name: ")
    marks = float(input("Enter marks: "))

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })

    save_students(students)
    print("Student added successfully!")


def view_students():
    students = read_students()

    if not students:
        print("No records found.")
        return

    for s in students:
        print(s)


def update_student():
    students = read_students()
    roll = int(input("Enter roll number to update: "))

    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")
            s["marks"] = float(input("Enter new marks: "))
            save_students(students)
            print("Record updated successfully!")
            return

    print("Student not found.")


def delete_student():
    students = read_students()
    roll = int(input("Enter roll number to delete: "))

    remaining = [s for s in students if s["roll"] != roll]

    if len(remaining) == len(students):
        print("Student not found.")
    else:
        save_students(remaining)
        print("Record deleted successfully!")


while True:
    print("\n1. Add")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter choice: ")

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
            print("Program ended.")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter valid numeric values.")
    except OSError as e:
        print("File error:", e)