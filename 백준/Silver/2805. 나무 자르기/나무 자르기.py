import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 1, max(trees)

while left <= right:
    mid = (left + right) // 2
    H = 0
    for tree in trees:
        if tree > mid:
            H += tree - mid

    if H >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)