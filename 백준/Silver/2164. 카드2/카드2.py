import sys
from collections import deque

dq = deque()
N = int(sys.stdin.readline())
dq = deque([i for i in range(1, N+1)])

while len(dq) > 1:
    dq.popleft()
    dq.append(dq[0])
    dq.popleft()

print(dq[0])