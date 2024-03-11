import sys
input = sys.stdin.readline

N = int(input())
dp, scores = [0 for _ in range(N)], []
for i in range(N):
    scores.append(int(input()))

if N == 1:
    print(scores[0])
elif N == 2:
    print(max(scores[0] + scores[1], scores[1]))
else:
    dp[0] = scores[0]
    dp[1] = max(scores[0] + scores[1], scores[1])
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])
    
    for i in range(3,N):
        #3개의 계단을 연속으로 밟을 수 없으므로 N번째 계단을 밟을 수 있는 경우는 아래 2가지
        #1. N-3, N-1번재 계단을 밟고 1칸 올라선 경우
        #2. N-2번째 계단을 밟고 2칸 올라선 경우
        dp[i] = max(dp[i-3] + scores[i-1], dp[i-2]) + scores[i]
    
    print(dp[-1])