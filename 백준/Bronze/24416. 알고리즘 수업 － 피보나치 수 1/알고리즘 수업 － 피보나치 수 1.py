import sys
#N번째 피보나치 재귀 함수의 카운트는 피보나치 수열(N)의 값과 같다.
def dp(n):
    F = [0,1,1]
    cnt = 0
    for i in range(3,n+1):
        cnt += 1
        F.append(F[i-1] + F[i-2])
    return F[n], cnt

N = int(sys.stdin.readline())
print(*dp(N))