import csv

files = ["students1.csv", "students2.csv"]

with open("combined.csv", "w", newline="") as output:
    writer = csv.writer(output)

    for i, filename in enumerate(files):
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)

            for j, row in enumerate(reader):
                if i == 0 or j > 0:
                    writer.writerow(row)

print("CSV files combined successfully.")