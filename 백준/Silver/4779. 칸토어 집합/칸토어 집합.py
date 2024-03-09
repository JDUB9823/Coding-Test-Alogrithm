import sys

def drawBlank(size):
    if size == 1:
        return "-"
    else:
        edge = drawBlank(size//3)
        center = " " * (size//3)
        return edge+center+edge

while True:
    N = sys.stdin.readline()
    if N == "":
        break
    else:
        print(drawBlank(3**int(N)))
        