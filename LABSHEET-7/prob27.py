import csv

with open("students.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print("Name:", row["Name"],
              "Marks:", row["Marks"])