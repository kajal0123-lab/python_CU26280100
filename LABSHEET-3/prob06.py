s = "hello"
frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)