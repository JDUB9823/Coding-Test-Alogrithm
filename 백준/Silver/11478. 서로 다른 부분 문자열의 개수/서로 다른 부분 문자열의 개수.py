import sys

S = sys.stdin.readline().rstrip()
subString = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        subString.add(S[i:j+1])

print(len(subString))