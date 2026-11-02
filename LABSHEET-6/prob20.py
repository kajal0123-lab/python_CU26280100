a = {1, 2}
b = {"A", "B"}

result = {(x, y) for x in a for y in b}

print(result)