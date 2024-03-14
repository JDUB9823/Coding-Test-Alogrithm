#A전봇대를 기준으로 정렬한 후 B전봇대에서 가장 긴 증가하는 부분 수열의 값을 구한다
import sys
input = sys.stdin.readline

N = int(input())
wires = sorted([list(map(int, input().split())) for _ in range(N)])
dp = [1] * (N)

for i in range(N):
    for j in range(i):
        if wires[i][1] > wires[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))