n = int(input())
k = int(input())
start, end = 0, n*n

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, n+1):
        count += mid // i if mid // i <= n else n

    if count < k:
        start = mid + 1
    else:
        end = mid - 1
print(end + 1)