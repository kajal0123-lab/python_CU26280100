f = open("sample.txt", "r")
lines = f.readlines()
f.close()

f = open("sample.txt", "w")

for line in lines:
    if line.strip():
        f.write(line)

f.close()
print("Blank lines removed.")