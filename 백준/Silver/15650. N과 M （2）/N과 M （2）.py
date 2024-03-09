import sys

def combination(idx):
    if len(res) == M:
        print(" ".join(map(str, res)))
        return
    else:
        for i in range(idx, N+1):
            if not visit[i]:
                visit[i] = 1
                res.append(i)
                combination(i+1)
                res.pop()
                visit[i] = 0


N, M = map(int, sys.stdin.readline().split())
visit = [False] * (N+1)
res = []
combination(1)