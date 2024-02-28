import sys

#유클리드 호제법을 이용한 최대공약수 구하기
def euclidean(x, y):
    while y > 0:
        x, y = y, x % y
    return x

N = int(sys.stdin.readline())

#A,B의 최소공배수 = (A x B) / 최대공약수
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    GCD = euclidean(max(x,y), min(x,y))
    print(x*y//GCD)