import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
count = 0

for i in reversed(range(n)):
    count += k // coin[i]
    k %= coin[i]

print(count)