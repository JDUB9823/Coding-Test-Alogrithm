import sys

primes = [0] * 2 + [1] * 999999

for i in range(2,len(primes)):
    if primes[i]:
        for j in range(2*i, len(primes), i):
            primes[j] = 0

T = int(sys.stdin.readline())
for _ in range(T):
    num = int(sys.stdin.readline())
    count = 0
    for i in range(2, num//2 + 1):
        if primes[i] and primes[num-i]:
            count += 1

    print(count)