import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
stack = deque()
for _ in range(N):
    cmd = list(input().split())

    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        print(-1 if not stack else stack.pop())
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(0 if stack else 1)
    elif cmd[0] == "top":
        print(-1 if not stack else stack[-1])