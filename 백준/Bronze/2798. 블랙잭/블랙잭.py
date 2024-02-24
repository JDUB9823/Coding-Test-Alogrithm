N, M = map(int, input().split())
cards = list(map(int, input().split()))

prevMax = 0
for i in range(len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)):
            cardSum = cards[i] + cards[j] + cards[k]
            if cardSum > prevMax and cardSum <= M:
                prevMax = cardSum

print(prevMax)