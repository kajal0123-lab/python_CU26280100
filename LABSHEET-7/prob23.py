import csv

total = 0
count = 0

with open("students.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        total += float(row["Marks"])
        count += 1

if count > 0:
    print("Average marks:", total / count)
else:
    print("No records found.")