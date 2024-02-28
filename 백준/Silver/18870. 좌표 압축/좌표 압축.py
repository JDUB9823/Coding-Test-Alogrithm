import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

#중복 제거 및 정렬
x = sorted(set(X))

dict = {x[i]:i for i in range(len(x))}

for i in X:
    print(dict[i], end=" ")