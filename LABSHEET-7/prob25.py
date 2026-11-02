import csv

with open("students.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Neha", 7, 88])

print("New record added successfully.")