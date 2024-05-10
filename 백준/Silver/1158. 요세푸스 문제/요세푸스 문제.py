import sys
input = sys.stdin.readline

N, K = map(int, input().split())
table = [i+1 for i in range(N)]
res = []
i = 0

while table:
    i += K - 1
    if i >= len(table):
        i %= len(table)
    res.append(table.pop(i))

print(str(res).replace("[", "<").replace("]", ">"))