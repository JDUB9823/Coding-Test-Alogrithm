import sys
input = sys.stdin.readline

aStr = " " + input().rstrip()
bStr = " " + input().rstrip()
DP = [[""] * len(bStr) for _ in range(len(aStr))]

for i in range(1, len(aStr)):
    for j in range(1, len(bStr)):
        if aStr[i] == bStr[j]:
            DP[i][j] = DP[i-1][j-1] + aStr[i]
        else:
            if len(DP[i-1][j]) > len(DP[i][j-1]):
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i][j-1]

print(len(DP[-1][-1]))
print(DP[-1][-1])