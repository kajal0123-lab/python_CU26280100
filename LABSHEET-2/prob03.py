n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if n >= 0 and total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")