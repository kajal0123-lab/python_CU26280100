numbers = [1, 2, 3, 2, 4, 3, 5]

seen = set()
duplicates = set()

for x in numbers:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

print("Duplicates:", duplicates)