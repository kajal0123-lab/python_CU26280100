n = int(input("Enter a number: "))
temp = abs(n)
total = 0

while temp > 0:
    total += temp % 10
    temp //= 10

print("Sum of digits:", total)