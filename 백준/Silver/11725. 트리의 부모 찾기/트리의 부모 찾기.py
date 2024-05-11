import sys
input = sys.stdin.readline

N = int(input())
edges = [[0] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    A, B = map(int, input().split())
    edges[A].append(B)
    edges[B].append(A)

q = [1]

while q:
    node = q.pop()
    for e in edges[node]:
        if parent[e] == 0:
            parent[e] = node
            q.append(e)

print("\n".join(map(str, parent[2:])))