f = open("sample.txt", "r")
data = f.read()
f.close()

print(data.upper())