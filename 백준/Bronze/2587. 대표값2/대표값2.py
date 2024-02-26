numbers = []

for _ in range(5):
    number = int(input())
    numbers.append(number)
numbers.sort()
print(sum(numbers) // 5)
print(numbers[2])