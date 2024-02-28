import sys

N = int(sys.stdin.readline())
positions = []

for _ in range(N):
    pos = list(map(int, sys.stdin.readline().split()))
    positions.append(pos)

positions.sort(key = lambda x: (x[1], x[0]))

for position in positions:
    print(*position)