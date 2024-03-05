import sys

N, K = map(int, sys.stdin.readline().split())
table = [i+1 for i in range(N)]
res = []
i = 0

while table:
    i += K - 1
    if i >= len(table):
        i %= len(table)
    res.append(table.pop(i))

print(str(res).replace("[","<").replace("]",">"))