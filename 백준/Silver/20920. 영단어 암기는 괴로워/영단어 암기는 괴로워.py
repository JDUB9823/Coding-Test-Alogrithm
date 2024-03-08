import sys

N, M = map(int, sys.stdin.readline().split())
vocab = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word in vocab:
            vocab[word] += 1
        else:
            vocab[word] = 1

vocab = sorted(vocab.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for v in vocab:
    print(v[0])