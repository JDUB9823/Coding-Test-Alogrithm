import sys
from collections import deque
input = sys.stdin.readline

def BFS(node, color):
    queue = deque([node])
    visited[node] = color

    while queue:
        n = queue.popleft()

        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = -1 * visited[n]
            elif visited[i] == visited[n]:
                return False
    return True
        
T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    queue = deque()
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    for i in range(1, V+1):
        if not visited[i]:
            res = BFS(i,1)
            if not res:
                break

    print("YES" if res else "NO")