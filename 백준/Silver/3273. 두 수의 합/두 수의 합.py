import sys
input = sys.stdin.readline

n = int(input())
series = sorted(list(map(int, input().split())))
x = int(input())

start, end, count = 0, n-1, 0

while start < end:
    sum = series[start] + series[end]

    if sum == x:
        count += 1
        start += 1
    elif sum < x:
        start += 1
    else:
        end -= 1

print(count)