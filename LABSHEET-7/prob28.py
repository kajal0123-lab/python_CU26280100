import csv

with open("students.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    students = list(reader)

if students:
    highest = max(students, key=lambda x: float(x["Marks"]))

    print("Student:", highest["Name"])
    print("Highest marks:", highest["Marks"])
else:
    print("No student records found.")