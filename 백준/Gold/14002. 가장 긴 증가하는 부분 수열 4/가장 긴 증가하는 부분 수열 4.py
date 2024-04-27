import sys
input = sys.stdin.readline

n = int(input())
series = list(map(int, input().split()))
DP = [1] * n
subsequence = []

for i in range(n):
    for j in range(i):
        if series[i] > series[j]:
            DP[i] = max(DP[i], DP[j] + 1)

turn = max(DP)
#부분수열 길이 출력
print(turn)

#맨 뒤에서부터 탐색
for i in range(n-1, -1, -1):
    if turn == DP[i]:
        subsequence.append(series[i])
        turn -= 1

print(*reversed(subsequence))