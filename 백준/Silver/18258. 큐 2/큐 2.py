import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        q.appendleft(int(command[1]))
    elif command[0] == "pop":
        if q:
            print(q[-1])
            q.pop()
        else:
            print(-1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        print(1 if not q else 0)
    elif command[0] == "front":
        print(q[-1] if q else -1)
    elif command[0] == "back":
        print(q[0] if q else -1)