N = int(input())
x, y = [], []

for _ in range(N):
    xpos, ypos = map(int, input().split())
    x.append(xpos)
    y.append(ypos)

print((max(x) - min(x)) * (max(y) - min(y)))