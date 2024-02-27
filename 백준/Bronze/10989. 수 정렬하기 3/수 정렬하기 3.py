import sys

N = int(sys.stdin.readline())
counts = [0] * 10001

for _ in range(N):
    number = int(sys.stdin.readline())
    counts[number] += 1

for (i,v) in enumerate(counts):
    if v != 0:
        for _ in range(v):
            print(i)