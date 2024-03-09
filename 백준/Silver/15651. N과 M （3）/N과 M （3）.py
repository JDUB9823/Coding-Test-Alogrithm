import sys

def permutation():
    if len(res) == M:
        print(" ".join(map(str, res)))
        return
    else:
        for i in range(1, N+1):
            res.append(i)
            permutation()
            res.pop()


N, M = map(int, sys.stdin.readline().split())
res = []
permutation()