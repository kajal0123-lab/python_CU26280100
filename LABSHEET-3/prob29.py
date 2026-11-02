list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6]

difference = []

for num in list1:
    if num not in list2:
        difference.append(num)

print("Difference:", difference)