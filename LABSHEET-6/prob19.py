from itertools import combinations

s = {1, 2, 3}
power_set = []

items = list(s)

for r in range(len(items) + 1):
    for c in combinations(items, r):
        power_set.append(set(c))

print(power_set)