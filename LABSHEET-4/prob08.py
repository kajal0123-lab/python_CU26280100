numbers = [2, 4, 3, 5, 7, 8]
target = 10

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])