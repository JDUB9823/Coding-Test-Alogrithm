import sys
input = sys.stdin.readline

def DFS(x, y, block):
    if visited[x][y] == 1:
        return
    if Map[x][y] == "0":
        return
        
    if block not in counts:
        counts[block] = 1
    else:
        counts[block] += 1
    visited[x][y] = 1
    
    if x > 0:
        DFS(x-1, y, block)
    if y > 0:
        DFS(x, y-1, block)
    if x < n-1:
        DFS(x+1, y, block)
    if y < n-1:
        DFS(x, y+1, block)

n = int(input())
Map = []
visited = [[0] * n for _ in range(n)]
counts = {}

for i in range(n):
    row = list(input().rstrip())
    Map.append(row)

for x in range(n):
    for y in range(n):
        if visited[x][y] == 0 and Map[x][y] == "1":
            DFS(x, y, len(counts) + 1)

counts = sorted(counts.items(), key = lambda item : item[1])
print(len(counts))
for count in counts:
    print(count[1])