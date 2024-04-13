import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def BFS():    
    while queue:
        pos = queue.popleft()
        if pos == 100:
            break

        for dice in range(1, 7):
            npos = pos + dice

            #다음 방문 위치가 100이내이고 첫 방문인 경우
            if npos < 101 and field[npos] == 0:
                field[npos] = field[pos] + 1
                #방문 위치에 사다리가 있는 경우
                if npos in ladders:
                    if field[ladders[npos]] == 0:
                        field[ladders[npos]] = field[npos]
                    else:
                        field[ladders[npos]] = min(field[ladders[npos]], field[npos])
                    npos = ladders[npos]
                #방문 위치에 뱀이 있는 경우
                if npos in snakes:
                    if field[snakes[npos]] == 0:
                        field[snakes[npos]] = field[npos]
                    else:
                        field[snakes[npos]] = min(field[snakes[npos]], field[npos])
                    npos = snakes[npos]
                queue.append(npos)
            
n, m = map(int, input().split())
ladders, snakes = {}, {}
field = [0] * 101
queue = deque([1])

for _ in range(n):
    s, e = map(int, input().split())
    ladders[s] = e

for _ in range(m):
    s, e = map(int, input().split())
    snakes[s] = e

BFS()
print(field[100])