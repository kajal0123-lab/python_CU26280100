marks = {
    "Aman": 85,
    "Riya": 92,
    "Rahul": 78
}

topper = max(marks, key=marks.get)

print("Highest marks student:", topper)
print("Marks:", marks[topper])