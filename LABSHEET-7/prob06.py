f = open("sample.txt", "r")

for i, line in enumerate(f, start=1):
    if i % 2 == 0:
        print(line, end="")

f.close()