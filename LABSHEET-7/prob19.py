f = open("sample.txt", "r")
words = f.read().split()
f.close()

words.sort(key=str.lower)

f = open("sorted.txt", "w")
f.write("\n".join(words))
f.close()

print("Words sorted and saved.")