N = int(input())
#도화지의 좌표는 모두 0으로 초기화
canvas = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    #주어진 좌표에 기반하여 가로 + 10, 세로 + 10까지의 좌표를 모두 1로 변경 
    for i in range(10):
        canvas[x + i][y:y+10] = [1,1,1,1,1,1,1,1,1,1]

#도화지 내부의 모든 1의 개수 = 도화지 내부의 색종이가 붙은 영역의 넓이
print(sum(row.count(1) for row in canvas))