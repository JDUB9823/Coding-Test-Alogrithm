def getP(x,y):
    return y * 100 // x

x,y = map(int, input().split())
z = getP(x,y)
MAX = 1000000000
start, end = 1, MAX

while start <= end:
    mid = (start + end) // 2
    Z = getP(x + mid, y + mid)

    if z >= Z:
        start = mid + 1
    else:
        end = mid - 1

if start > MAX:
    print(-1)
else:
    print(start)