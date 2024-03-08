import sys

N = int(sys.stdin.readline())
count = 0
log = set()

for _ in range(N):
    entry = sys.stdin.readline().rstrip()

    if entry == "ENTER":
        count += len(log)
        log = set()
    else:
        log.add(entry)

count += len(log)
print(count)