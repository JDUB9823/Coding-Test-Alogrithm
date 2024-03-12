import sys
input = sys.stdin.readline

def getSum(num):
    s = [0, num[0]]
    for i in range(1, len(num)):
        s.append(s[i] + num[i])
    return s

N, M = map(int, input().split())
num = list(map(int, input().split()))
sum = getSum(num)

for _ in range(M):
    start, end = map(int, input().split())
    print(sum[end] - sum[start-1])