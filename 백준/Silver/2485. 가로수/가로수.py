import sys

def euclidean(x, y):
    while y > 0:
        x, y = y,  x % y
    return x

N = int(sys.stdin.readline())
trees = sorted([int(sys.stdin.readline()) for _ in range(N)])
#나무들의 간격 구해서 저장
diff = [trees[i+1] - trees[i] for i in range(N-1)]
gcd = diff[0]

#모든 나무 간격의 최대공약수 구하기
for i in range(1,len(diff)):
    gcd = euclidean(gcd, diff[i])

count = 0
for dif in diff:
    count += dif//gcd - 1

print(count)