import sys
input = sys.stdin.readline

def DP(i, w):
    #추의 index를 넘어가거나, 방문한 무게를 다른 추로 구할 수 있는 경우 계산X
    if i > n:
        return
    if dp[i][w] == 1:
        return

    dp[i][w] = 1
    #현재 추를 저울에 올리지 않는 경우
    DP(i + 1, w)
    #현재 추를 구슬의 반대편에 올리는 경우
    DP(i + 1, w + weight[i-1])
    #현재 추를 구슬과 같이 저울에 올리는 경우
    DP(i + 1, abs(w - weight[i-1]))

n, weight = int(input()), list(map(int, input().split()))
m, marvels = int(input()), list(map(int, input().split()))

#추의 max weight = 500g, max count = 30
dp = [[0] * 15001 for _ in range(31)]
DP(0,0)

for marvel in marvels:
    if marvel > 15000:
        print("N", end = " ")
    elif dp[n][marvel]:
        print("Y", end = " ")
    else:
        print("N", end = " ")