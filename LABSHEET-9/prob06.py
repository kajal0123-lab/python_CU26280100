employees = {}

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))

        if emp_id in employees:
            print("Employee ID already exists.")
        else:
            employees[emp_id] = {
                "name": name,
                "salary": salary
            }
            print("Employee added successfully!")

    elif choice == "2":
        if employees:
            for emp_id, details in employees.items():
                print(emp_id, details)
        else:
            print("No employees found.")

    elif choice == "3":
        emp_id = input("Enter employee ID to update: ")

        if emp_id in employees:
            employees[emp_id]["name"] = input("Enter new name: ")
            employees[emp_id]["salary"] = float(
                input("Enter new salary: ")
            )
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    elif choice == "4":
        emp_id = input("Enter employee ID to delete: ")

        if emp_id in employees:
            del employees[emp_id]
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice!")