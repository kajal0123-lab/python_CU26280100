f = open("sample.txt", "r")
data = f.read()
f.close()

word = input("Enter the word to search: ")

if word.lower() in data.lower().split():
    print("Word found.")
else:
    print("Word not found.")