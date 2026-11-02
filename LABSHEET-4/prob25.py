paragraph = "Python is easy. Python is powerful."

words = paragraph.lower().replace(".", "").split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)