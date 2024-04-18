import sys
from collections import deque
input = sys.stdin.readline
MAX = 100001

def BFS():
    while queue:
        pos = queue.popleft()
        #순간이동은 시간추가 X
        if pos * 2 < MAX and not visited[pos*2]:
            queue.appendleft(pos*2)
            visited[pos*2] = 1
            distance[pos*2] = distance[pos]
        if pos - 1 >= 0 and not visited[pos-1]:
            queue.append(pos-1)
            visited[pos-1] = 1
            distance[pos-1] = distance[pos] + 1
        if pos + 1 < MAX and not visited[pos+1]:
            queue.append(pos+1)
            visited[pos+1] = 1
            distance[pos+1] = distance[pos] + 1
    return distance[k]

n, k = map(int, input().split())
visited = [0] * MAX
distance = [0] * MAX
queue = deque([n])
visited[n] = 1

print(BFS())