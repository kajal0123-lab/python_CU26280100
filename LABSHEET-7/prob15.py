f = open("sample.txt", "r")
data = f.read()
f.close()

old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

data = data.replace(old_word, new_word)

f = open("sample.txt", "w")
f.write(data)
f.close()

print("Word replaced successfully.")