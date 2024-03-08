import sys

N = int(sys.stdin.readline())
log = set()
log.add("ChongChong")

for _ in range(N):
    a, b = sys.stdin.readline().split()
    if a in log and b not in log:
        log.add(b)
    elif a not in log and b in log:
        log.add(a)

print(len(log))