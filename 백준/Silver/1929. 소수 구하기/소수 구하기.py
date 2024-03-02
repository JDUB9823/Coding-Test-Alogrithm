import sys

def checkPrime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True

M, N = map(int, sys.stdin.readline().split())
for num in range(M, N+1):
    if num == 1:
        continue
    if checkPrime(num):
        print(num)