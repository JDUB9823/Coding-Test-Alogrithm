import sys
input = sys.stdin.readline
INF = sys.maxsize

def binarysearch(left, right, target):
    while left < right:
        mid = (left + right) // 2

        if LIS[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

n = int(input())
series = list(map(int, input().split()))

LIS = [-INF]
LIS_step = [(-INF, 0)] #val, idx

#LIS 알고리즘 적용
for num in series:
    #현재 숫자가 LIS 배열의 마지막 값보다 크면, LIS 배열에 삽입
    if num > LIS[-1]:
        LIS_step.append((num, len(LIS)))
        LIS.append(num)
        
    #현재 숫자가 LIS 배열의 마지막 값보다 작으면, 이분탐색을 통해 LIS 배열의 중간에 삽입
    else:
        idx = binarysearch(0, len(LIS), num)
        LIS[idx] = num
        LIS_step.append((num, idx))

LIS_order = len(LIS) - 1
LIS_res = []

print(LIS_order)

while LIS_order:
    num, idx = LIS_step.pop()
    if idx == LIS_order:
        LIS_res.append(num)
        LIS_order -= 1

print(*reversed(LIS_res))