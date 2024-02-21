X = int(input())

#X가 포함된 n번째 대각선(nthDiagonal)의 가장 큰 X인 maxX를 구한다.
nthDiagonal, maxX = 1, 1
while X > maxX:
    nthDiagonal += 1
    maxX += nthDiagonal

#대각선의 n이 짝수인 경우, 대각선 위에서 아래로 진행
if nthDiagonal % 2 == 0:
    print(f"{nthDiagonal - (maxX - X)}/{(maxX - X) + 1}")
#1행 기준 maxX가 홀수인 경우, 대각선 아래에서 위로 진행
else:
    print(f"{(maxX - X) + 1}/{nthDiagonal - (maxX - X)}")