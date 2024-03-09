import sys
from collections import deque

def permutation(n, m):
    if len(dq) == m:
        for num in dq:
            print(num, end=" ")
        print()
        return
    else:
        for i in range(1, N+1):
            if not visit[i]:
                visit[i] = 1
                dq.append(i)
                permutation(n,m)
                dq.pop()
                visit[i] = 0

visit = [0] * 9
dq = deque()
N, M = map(int, sys.stdin.readline().split())
permutation(N, M)