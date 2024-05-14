import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def findParent(child):
    if parents[child] != child:
        parents[child] = findParent(parents[child])
    return parents[child]

def unionParents(a, b):
    A = findParent(a)
    B = findParent(b)

    #값이 더 작은 노드가 부모로
    if A > B:
        parents[A] = B
    else:
        parents[B] = A
        

N, M = map(int, input().split())
parents = [i for i in range(N+1)]

for _ in range(M):
    cmd, A, B = map(int, input().split())

    if cmd == 0:
        unionParents(A, B)
    else:
        print("YES" if findParent(A) == findParent(B) else "NO")