import sys

def checkPrime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    while True:
        if num == 0 or num == 1 or num == 2:
            print(2)
            break
        if checkPrime(num):
            print(num)
            break
        num += 1