students = [
    {"roll": 1, "name": "Rahul", "marks": 85},
    {"roll": 2, "name": "Priya", "marks": 92},
    {"roll": 3, "name": "Amit", "marks": 78}
]

roll_no = int(input("Enter roll number: "))
found = False

for student in students:
    if student["roll"] == roll_no:
        new_marks = float(input("Enter new marks: "))
        student["marks"] = new_marks
        print("Marks updated successfully!")
        found = True
        break

if not found:
    print("Student not found.")

print(students)