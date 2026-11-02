a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = abs(a), abs(b)

if a == 0 or b == 0:
    lcm = 0
else:
    lcm = max(a, b)

    while lcm % a != 0 or lcm % b != 0:
        lcm += 1

print("LCM:", lcm)