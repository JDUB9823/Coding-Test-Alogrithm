import sys

#선형 탐색은 500,000^2 = 2억5천(약 2.5초) 시간 제한이 2초이므로 NlogN인 이진탐색으로 진행
def binarySearch(arr, start, end, cur):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == cur:
            return True
        elif arr[mid] > cur:
            end = mid - 1
        else:
            start = mid + 1
    return False

N = int(sys.stdin.readline())
hand = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

#이진 탐색을 위해 배열 정렬
hand.sort()

for card in cards:
    print(int(binarySearch(hand, 0, N-1, card)), end=" ")