t1  = (10, 20, 30, 40)
t2 = (1, 2, 3, 4)

result = tuple(a + b for a, b in zip(t1,t2))

print("first tuple:", t1)
print("second tuple:", t2)
print("Element-wise sum:", result)