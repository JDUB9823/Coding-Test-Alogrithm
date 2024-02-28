import sys

N = int(sys.stdin.readline())
words = [sys.stdin.readline().replace("\n", "") for _ in range(N)]

#중복 제거
words = list(set(words))
#길이 순으로 정렬
words.sort()
#사전순으로 정렬
words.sort(key=lambda x: len(x))

for word in words:
    print(word)