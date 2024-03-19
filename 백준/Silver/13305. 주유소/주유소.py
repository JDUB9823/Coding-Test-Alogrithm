import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
p = sys.maxsize
res = 0

for i in range(n-1):
    p = min(p, price[i])
    res += p * dist[i]

print(res)