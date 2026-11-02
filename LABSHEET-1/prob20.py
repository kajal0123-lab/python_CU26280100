total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks for subject {i}: "))
    total += marks

percentage = (total / 500) * 100

print("Total marks:", total)
print("Percentage:", percentage, "%")