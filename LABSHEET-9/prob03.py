students = [
    {"roll": 1, "name": "Rahul", "marks": 85},
    {"roll": 2, "name": "Priya", "marks": 92},
    {"roll": 3, "name": "Amit", "marks": 78}
]

search_name = input("Enter student name to search: ").strip()

found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("Student found:", student)
        found = True

if not found:
    print("Student not found.")