import sys

S = sys.stdin.readline().split("-")

for i in range(len(S)):
    temp = list(map(int, S[i].split("+")))
    S[i] = sum(temp)
res = S[0]

for j in range(1, len(S)):
    res -= S[j]
print(res)