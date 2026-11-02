text = "programming"
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)