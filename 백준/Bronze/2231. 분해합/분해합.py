N = int(input())

result = 0
for i in range(N//2, N):
    constructor = [int(num) for num in str(i)]
    if i + sum(constructor) == N:
        result = i
        break

print(result)