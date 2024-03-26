import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(hq, x)
    else:
        print(heapq.heappop(hq) if hq else 0)