import sys
input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
minCount = [[0] * n for _ in range(n)]

for size in range(1, n):
    for start in range(n):
        end = start + size
        if end >= n:
            break
        minCount[start][end] = sys.maxsize
        for cur in range(start, end):
            minCount[start][end] = min(minCount[start][end], minCount[start][cur] + minCount[cur+1][end] + matrix[start][0] * matrix[cur][1] * matrix[end][1])

print(minCount[0][-1])