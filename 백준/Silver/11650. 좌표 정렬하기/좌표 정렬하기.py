N = int(input())
positions = []

for _ in range(N):
    pos = list(map(int, input().split()))
    positions.append(pos)

positions.sort()

for position in positions:
    print(*position)