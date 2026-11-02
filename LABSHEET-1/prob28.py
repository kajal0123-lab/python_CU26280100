ch = input("Enter a character: ")

if len(ch) != 1:
    print("Enter only one character")
elif ch.isupper():
    print("Uppercase character")
elif ch.islower():
    print("Lowercase character")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")