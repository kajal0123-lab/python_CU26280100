f = open("sample.txt", "r")
data = f.read()

lines = data.splitlines()
print("Number of lines:", len(lines))
print("Number of characters:", len(data))

f.close()