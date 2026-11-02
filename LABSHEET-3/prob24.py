numbers = [1, 2, 3, 4, 5]
reverse = []

for i in range(len(numbers) - 1, -1, -1):
    reverse.append(numbers[i])

print("Reversed list:", reverse)