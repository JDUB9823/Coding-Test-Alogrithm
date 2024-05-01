import sys
from collections import deque
input = sys.stdin.readline

def BFS(start, target):
    queue = deque()
    queue.append([start, ""])

    while queue:
        num, cmd = queue.popleft()
        if num == target:
            print(cmd)
            break

        #D command
        dNum = (num * 2) % 10000
        if visited[dNum] == 0:
            visited[dNum] = True
            queue.append([dNum, cmd + "D"])

        #S command
        sNum = num - 1 if num != 0 else 9999
        if not visited[sNum]:
            visited[sNum] = True
            queue.append([sNum, cmd + "S"])

        #L command
        lStr = str(num).zfill(4)
        lNum = int(lStr[1:] + lStr[0])
        if not visited[lNum]:
            visited[lNum] = True
            queue.append([lNum, cmd + "L"])

        #R command
        rStr = str(num).zfill(4)
        rNum = int(rStr[-1] + rStr[:3])
        if not visited[rNum]:
            visited[rNum] = True
            queue.append([rNum, cmd + "R"])
            

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10000
    visited[A] = True

    BFS(A, B)