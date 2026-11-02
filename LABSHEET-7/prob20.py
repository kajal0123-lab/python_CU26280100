f1 = open("file1.txt", "r")
data1 = f1.read()
f1.close()

f2 = open("file2.txt", "r")
data2 = f2.read()
f2.close()

f3 = open("merged.txt", "w")
f3.write(data1)

if data1 and data2 and not data1.endswith("\n"):
    f3.write("\n")

f3.write(data2)
f3.close()

print("Files merged successfully.")