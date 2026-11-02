base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1

if exponent >= 0:
    for i in range(exponent):
        result *= base
else:
    if base == 0:
        print("Undefined result")
    else:
        for i in range(-exponent):
            result *= base
        result = 1 / result

if exponent >= 0 or base != 0:
    print("Result:", result)