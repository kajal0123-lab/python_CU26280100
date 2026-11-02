n = int(input("Enter a number: "))
temp = abs(n)
count = 0

if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10

print("Number of digits:", count)