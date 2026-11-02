f = open("sample.txt", "r")
lines = f.readlines()
f.close()

if lines:
    print("First line:", lines[0], end="")
    if len(lines) > 1:
        print("Last line:", lines[-1], end="")
    else:
        print("This is also the last line.")
else:
    print("File is empty.")