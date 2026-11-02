s = "python is an easy language"
result = ""
new_word = True

for ch in s:
    if ch == " ":
        result += ch
        new_word = True
    elif new_word:
        result += chr(ord(ch) - 32) if 'a' <= ch <= 'z' else ch
        new_word = False
    else:
        result += ch

print(result)