import sys
input = sys.stdin.readline

def findNum(n,s,e):
    while s <= e:
        mid = (s + e) // 2
        if A[mid] == n:
            return 1
        elif A[mid] < n:
            s = mid + 1
        else:
            e = mid - 1
    else:
        return 0

t = int(input())
for _ in range(t):
    n = int(input())
    A = sorted(list(map(int, input().split())))
    m = int(input())
    B = list(map(int, input().split()))
    for b in B:
        start, end = 0, n - 1
        print(findNum(b,start,end))