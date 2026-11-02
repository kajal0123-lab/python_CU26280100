s = input("Enter a sentence: ").lower()
words = s.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

if frequency:
    most_repeated = max(frequency, key=frequency.get)
    print("Most repeated word:", most_repeated)
    print("Frequency:", frequency[most_repeated])
else:
    print("No words found")