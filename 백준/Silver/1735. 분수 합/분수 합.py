import sys

def euclidean(x, y):
    while y > 0:
        x, y = y, x % y
    return x

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

resA, resB = a1*b2 + a2*b1, b1*b2
GCD = euclidean(resA, resB)
print(resA//GCD, resB//GCD)