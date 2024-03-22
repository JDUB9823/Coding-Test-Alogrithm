import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int, input().split())))
m = int(input())
B = list(map(int, input().split()))
hand = {}

for card in A:
    if card in hand:
        hand[card] += 1
    else:
        hand[card] = 1

for card in B:
    left, right = 0, n-1

    while left <= right:
        mid = (left + right) // 2
        if card == A[mid]:
            print(hand.get(card), end = " ")
            break
        elif card <= A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        print(0, end = " ")