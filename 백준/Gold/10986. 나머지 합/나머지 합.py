import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split())) + [0]
R = [0]*M

for i in range(N):
    A[i] += A[i-1] #누적 합 구하기
    R[A[i] % M] += 1 # 누적합을 M으로 나눈 나머지를 index로 하는 숫자의 개수 더하기

count = R[0] #나머지가 0인 숫자는 M으로 나누어 지므로 카운트에 바로 반영
#나머지가 0이 아닌 수는 2개의 숫자 조합으로 count에 반영
#ex) M = 3이고 누적합이 1, 7인 경우 나머지는 각각 1이므로 7-1을 하면 M으로 나누어짐
for r in R:
    count += r * (r-1) // 2 #조합 공식 = (N*(N-1))/2
print(count)