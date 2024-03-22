import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int, input().split())))
m = int(input())
B = list(map(int, input().split()))

for num in B:
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if num == A[mid]:
            print(1)
            break
        elif num <= A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        print(0)