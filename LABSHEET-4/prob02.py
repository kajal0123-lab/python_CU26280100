numbers = [1, 2, 3, 4, 5]
n = 2

n = n % len(numbers)
rotated = numbers[-n:] + numbers[:-n]

print("Rotated list:", rotated)