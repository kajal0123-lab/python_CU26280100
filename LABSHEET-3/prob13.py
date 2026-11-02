s = "Hello World"
result = ""

for ch in s:
    if ch.lower() in "aeiou":
        result += ch.upper()
    elif ch.isalpha():
        result += ch.lower()
    else:
        result += ch

print(result)