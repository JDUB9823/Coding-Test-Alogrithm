import sys
input = sys.stdin.readline

N, K = map(int, input().split())
item, bag = [], [0 for _ in range(K+1)]
for _ in range(N):
    item.append(list(map(int, input().split())))

for w, v in item:
    for i in range(K, w-1, -1):
        bag[i] = max(bag[i], bag[i-w]+v)

print(bag[-1])