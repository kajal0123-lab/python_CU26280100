import csv

with open("students.csv", "r", newline="") as f1:
    data = list(csv.reader(f1))

with open("students_copy.csv", "w", newline="") as f2:
    writer = csv.writer(f2)
    writer.writerows(data)

print("CSV data copied successfully.")