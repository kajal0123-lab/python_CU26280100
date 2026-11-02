data = [(1, "A"), (2, "B"), (3, "C")]

numbers, letters = zip(*data)

numbers = list(numbers)
letters = list(letters)

print("Numbers:", numbers)
print("Letters:", letters)