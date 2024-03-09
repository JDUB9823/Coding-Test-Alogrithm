#a,b,c는 각각의 기둥
def hanoi(n,a,b,c):
    if n==1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)

N = int(input())
#원판의 총 이동 개수
print(2**N-1)
hanoi(N,1,2,3)