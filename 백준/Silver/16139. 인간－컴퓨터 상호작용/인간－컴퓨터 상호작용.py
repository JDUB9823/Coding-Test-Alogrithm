import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())
PS = [[0] * 26 for i in range(len(s))]

for i in range(len(s)):
    PS[i][ord(s[i])-ord('a')] = 1
    if i >= 1:
        for j in range(26):
            PS[i][j] += PS[i-1][j]

for _ in range(q):
    a,l,r = map(str, input().split())
    if int(l) == 0:
        print(PS[int(r)][ord(a) - 97])
    else:
        print(PS[int(r)][ord(a) - 97] - PS[int(l) - 1][ord(a) - 97])