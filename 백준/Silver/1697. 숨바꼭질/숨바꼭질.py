import sys
from collections import deque
input = sys.stdin.readline

def BFS(pos):
    queue = deque()
    queue.append(pos)
    while queue:
        pos = queue.popleft()
        if pos == k:
            break

        for npos in (pos-1, pos+1, pos*2):
            if 0 <= npos <= 100000 and not visited[npos]:
                visited[npos] = visited[pos] + 1
                queue.append(npos)
    return

n, k = map(int, input().split())
visited = [0] * 100001
visited[n] = 0
BFS(n)

print(visited[k])