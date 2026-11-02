import string

s = "Hello, World! Python is easy."
result = ""

for ch in s:
    if ch not in string.punctuation:
        result += ch

print(result)