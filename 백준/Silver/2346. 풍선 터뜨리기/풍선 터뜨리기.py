import sys
from collections import deque

N = int(sys.stdin.readline())
ballons = deque(enumerate(map(int, sys.stdin.readline().split())))
res = []

for _ in range(N):
    i, v = ballons.popleft()
    res.append(i+1)
    if v > 0:
        ballons.rotate(-v + 1)
    else:
        ballons.rotate(-v)

print(*res)