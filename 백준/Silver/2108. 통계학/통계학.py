import sys

def average(num, N):
    return round(sum(num)/N)

def median(num, N):
    return num[N//2]

def mode(num):
    counts = {}
    for n in num:
        counts[n] = counts.get(n, 0) + 1

    mode = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    if len(mode) == 1 or counts[mode[0][0]] != counts[mode[1][0]]:
        return mode[0][0]
    else:
        return mode[1][0]
        
def difference(num):
    return num[-1] - num[0]


N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]
num.sort()

print(average(num, N))
print(median(num, N))
print(mode(num))
print(difference(num))