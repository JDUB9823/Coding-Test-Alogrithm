import sys

N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for num in numbers:
    print(num)