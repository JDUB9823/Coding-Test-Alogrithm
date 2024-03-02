import sys

def checkPrime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True

primes = [0] * (123456 *2 + 1)

for i in range(2,len(primes)):
    if checkPrime(i) == True:
        primes[i] = 1

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    print(sum(primes[N+1:2*N + 1]))