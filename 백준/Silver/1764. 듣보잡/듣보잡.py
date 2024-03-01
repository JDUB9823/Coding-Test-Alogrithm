import sys

N, M = map(int, sys.stdin.readline().split())
neverSeen = set(sys.stdin.readline().rstrip() for _ in range(N))
neverHeard = set(sys.stdin.readline().rstrip() for _ in range(M))

neverSeenAndHeard = sorted(neverSeen.intersection(neverHeard))

print(len(neverSeenAndHeard))
for name in neverSeenAndHeard:
    print(name)