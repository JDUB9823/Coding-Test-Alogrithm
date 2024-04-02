n = int(input())
A = list(map(int, input().split()))
res = [-1] * n
stack = []
counter = {}

for a in A:
    if a in counter:
        counter[a] += 1
    else:
        counter[a] = 1

for i in range(n):
    while stack and counter[A[stack[-1]]] < counter[A[i]]:
        res[stack.pop()] = A[i]
    stack.append(i)

print(*res)