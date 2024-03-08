import sys

def fibo(f, num):
    for n in range(2, num):
        f.append(f[n]+f[n-1])
    return f[num]

N = int(sys.stdin.readline())
print(fibo([0,1,1], N))