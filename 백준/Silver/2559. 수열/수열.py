import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temperature = list(map(int, input().split()))
PS = []
PS.append(sum(temperature[:k]))

for i in range(k,n):
    PS.append(PS[i-k]+temperature[i]-temperature[i-k])

print(max(PS))