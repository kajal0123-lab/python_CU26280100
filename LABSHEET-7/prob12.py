f = open("sample.txt", "r")
data = f.read()
f.close()

word = input("Enter the word: ")

words = data.lower().split()
count = words.count(word.lower())

print("Occurrences:", count)