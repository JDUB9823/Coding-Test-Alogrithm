import sys
input = sys.stdin.readline

n, c = map(int, input().split())
dist = sorted([int(input()) for _ in range(n)])
left, right = 1, max(dist)

while left <= right:
    mid = (left + right) // 2
    router, current = 1, dist[0]

    for i in range(1, n):
        if dist[i] >= current + mid:
            router += 1
            current = dist[i]
    if router >= c:
        left = mid + 1
    else:
        right = mid - 1

print(right)