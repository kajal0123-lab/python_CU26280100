f = open("sample.txt", "r")
lines = f.readlines()
f.close()

if lines:
    longest = max(lines, key=len)
    print("Longest line:", longest, end="")
else:
    print("File is empty.")