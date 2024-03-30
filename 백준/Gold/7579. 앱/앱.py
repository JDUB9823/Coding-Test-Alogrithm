import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [0] +list(map(int, input().split()))
C = [0] + list(map(int, input().split()))
dp = [[0] * (sum(C) + 1) for _ in range(n + 1)]
res = sys.maxsize

for i in range(1, n + 1):
    mem, cost = A[i], C[i]
    for curCost in range(sum(C) + 1):
        #현재 cost가 비활성화 하려는 앱의 cost보다 낮은 경우, 비활성화한 기존 cost 유지
        if curCost < cost:
            dp[i][curCost] = dp[i-1][curCost]
        #현재 cost => 비활성화 cost인 경우, 현재 cost에서 확보할 수 있는 최대 메모리 계산
        else:
            dp[i][curCost] = max(dp[i-1][curCost], dp[i-1][curCost-cost] + mem)
        
        #m이상의 메모리를 확보한 경우, 최소 cost 값 비교
        if dp[i][curCost] >= m:
            res = min(res, curCost)
        
print(res)