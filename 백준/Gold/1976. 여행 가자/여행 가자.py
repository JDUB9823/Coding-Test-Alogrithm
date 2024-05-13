import sys
input = sys.stdin.readline

def find(city):
    if city != parents[city]:
        parents[city] = find(parents[city])
    return parents[city]

def union(a, b):
    A = find(a)
    B = find(b)

    #값이 더 작은 노드가 부모로
    if A > B:
        parents[A] = B
    else:
        parents[B] = A

N, M = int(input()), int(input())
parents = [i for i in range(N+1)]

links = []
for i in range(N):
    links.append(list(map(int, input().split())))
    for j in range(N):
        if links[i][j] == 1:
            union(i+1, j+1)

plan = list(map(int, input().split()))
root = find(plan[0])
#중복된 계획 제거
plan = list(set(plan))[1:]
flag = True

for city in plan:
    if root != find(city):
        flag = False
        break

print("YES" if flag else "NO")