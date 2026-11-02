f = open("sample.txt", "r")
data = f.read()

words = data.split()
print("Number of words:", len(words))

f.close()