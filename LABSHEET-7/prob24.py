import csv

with open("students.csv", "r", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

if data:
    print("Number of rows:", len(data) - 1)
    print("Number of columns:", len(data[0]))
else:
    print("CSV file is empty.")