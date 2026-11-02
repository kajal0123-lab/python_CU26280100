f = open("sample.txt", "r")
words = f.read().split()
f.close()

unique_words = list(dict.fromkeys(words))

f = open("unique.txt", "w")
f.write(" ".join(unique_words))
f.close()

print("Unique words saved.")