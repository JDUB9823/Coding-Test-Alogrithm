import sys

def C(idx):
    if len(res) == M:
        print(" ".join(map(str, res)))
        return
    else:
        for i in range(idx, N+1):
            res.append(i)
            C(i)
            res.pop()

N, M = map(int, sys.stdin.readline().split())
res = []
C(1)