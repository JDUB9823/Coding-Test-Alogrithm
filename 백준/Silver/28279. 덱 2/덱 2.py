import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "1":
        dq.appendleft(int(command[1]))
    elif command[0] == "2":
        dq.append(int(command[1]))
    elif command[0] == "3":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == "4":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif command[0] == "5":
        print(len(dq))
    elif command[0] == "6":
        print(0 if dq else 1)
    elif command[0] == "7":
        print(dq[0] if dq else -1)
    elif command[0] == "8":
        print(dq[-1] if dq else -1)