angles = [int(input()) for _ in range(3)]

#3각의 합이 180이 아닌 경우
if sum(angles) != 180:
    print("Error")
else:
    #정삼각형인 경우
    if angles.count(60) == 3:
        print("Equilateral")
    #이등변삼각형인 경우
    elif len(set(angles)) == 2:
        print("Isosceles")
    else:
        print("Scalene")