numbers = [10, 20, 40, 30, 40]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second largest:", unique_numbers[-2])
else:
    print("No second largest number")