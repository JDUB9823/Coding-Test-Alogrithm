import sys

N = int(sys.stdin.readline())
hand = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

#손에 든 카드를 {카드: 카드 count}로 변환
handDict = {}
for card in hand:
    if card in handDict:
        handDict[card] += 1
    else:
        handDict[card] = 1

for card in cards:
    if card in handDict:
        print(handDict[card], end=" ")
    else:
        print(0, end=" ")