import csv

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["Name", "Class", "Marks"])
    writer.writerow(["Aman", 7, 85])
    writer.writerow(["Riya", 7, 92])
    writer.writerow(["Rahul", 7, 78])

print("CSV file created successfully.")