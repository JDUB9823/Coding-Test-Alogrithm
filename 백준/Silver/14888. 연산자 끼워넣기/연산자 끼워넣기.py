import sys
#식의 결과 값은 -10억 ~ 10억
MAX = 1000000000

def backtrace(cnt, prev, add, sub, mul, div):
    if cnt == N:
        res[0] = max(res[0], prev)
        res[1] = min(res[1], prev)

    if add > 0:
        backtrace(cnt+1, prev+num[cnt], add-1, sub, mul, div)
    if sub > 0:
        backtrace(cnt+1, prev-num[cnt], add, sub-1, mul, div)
    if mul > 0:
        backtrace(cnt+1, prev*num[cnt], add, sub, mul-1, div)
    if div > 0:
        if prev < 0:
            backtrace(cnt+1, -(-prev//num[cnt]), add, sub, mul, div-1)
        else:
            backtrace(cnt+1, prev//num[cnt], add, sub, mul, div-1)

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
#res[0] = max, res[1] = min
res= [-MAX, MAX]

backtrace(1, num[0], op[0], op[1], op[2], op[3])

print(*res)