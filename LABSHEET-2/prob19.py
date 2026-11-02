n = int(input("Enter a number: "))
temp = abs(n)
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if n < 0:
    reverse = -reverse

print("Reversed number:", reverse)