import sys
from collections import deque
input = sys.stdin.readline
LIMIT = 100001

def BFS(pos):
    queue = deque()
    queue.append(pos)

    while queue:
        pos = queue.popleft()
        if pos == K:
            break

        for npos in (pos-1, pos+1, pos*2):
            if 0 <= npos < LIMIT and visited[npos][0] == 0:
                visited[npos] = visited[pos][0]+1, pos
                queue.append(npos)
    return

N, K = map(int, input().split())
#걸린 시간, 이전 위치
visited =  [[0, -1]] * LIMIT

BFS(N)

res = [K]
prevPos = K

while len(res) != visited[K][0] + 1:
    prevPos = visited[prevPos][1]
    res.append(prevPos)

print(visited[K][0])
print(*res[::-1])