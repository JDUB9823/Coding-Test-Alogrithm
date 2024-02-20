x, y = [], []

for _ in range(3):
    xpos, ypos = map(int, input().split())
    x.append(xpos)
    y.append(ypos)

print(min(x, key = x.count), min(y, key = y.count))