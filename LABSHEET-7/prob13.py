f = open("numbers.txt", "r")
data = f.read()
f.close()

numbers = list(map(float, data.split()))

if len(numbers) > 0:
    total = sum(numbers)
    average = total / len(numbers)

    print("Sum:", total)
    print("Average:", average)
else:
    print("No numbers found.")