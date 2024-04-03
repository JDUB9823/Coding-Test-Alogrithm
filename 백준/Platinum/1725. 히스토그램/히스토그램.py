import sys
input = sys.stdin.readline

n = int(input())
stack = []
area = 0

for i in range(n):
    height, width = int(input()), i
    #stack의 높이 >= 현재 높이의 경우, 더 이상 사각형의 넓이가 확장되지 않음
    while stack and stack[-1][1] >= height:
        width, prevHeight = stack.pop()
        area = max(area, (i - width) * prevHeight)
    stack.append([width, height])

#만약 모든 입력의 높이가 같을 경우
while stack:
    width, height = stack.pop()
    area = max(area, (n - width) * height)

print(area)