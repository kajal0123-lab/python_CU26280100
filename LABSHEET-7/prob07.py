f = open("sample.txt", "w")

n = int(input("How many lines do you want to enter? "))

for i in range(n):
    line = input("Enter a line: ")
    f.write(line + "\n")

f.close()
print("Data saved successfully.")