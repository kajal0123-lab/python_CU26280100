n = int(input("Enter a number: "))
total = 0

for i in range(1, n):
    if n > 0 and n % i == 0:
        total += i

if n > 0 and total == n:
    print("Perfect number")
else:
    print("Not a perfect number")