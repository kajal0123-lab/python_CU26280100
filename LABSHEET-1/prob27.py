ch = input("Enter a character: ")

if len(ch) != 1 or not ch.isalpha():
    print("Enter a single alphabet")
elif ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")