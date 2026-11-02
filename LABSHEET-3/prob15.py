s = "swiss"

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeated character:", ch)
        break
else:
    print("No non-repeated character")