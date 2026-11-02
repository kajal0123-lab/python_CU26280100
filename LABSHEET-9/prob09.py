# Write student data to a text file
with open("students.txt", "w") as file:
    file.write("1,Rahul,85\n")
    file.write("2,Priya,92\n")
    file.write("3,Amit,78\n")

print("Student data saved successfully!")

# Read student data from the file
with open("students.txt", "r") as file:
    print("\nStudent Records:")

    for line in file:
        roll, name, marks = line.strip().split(",")
        print("Roll:", roll, "Name:", name, "Marks:", marks)