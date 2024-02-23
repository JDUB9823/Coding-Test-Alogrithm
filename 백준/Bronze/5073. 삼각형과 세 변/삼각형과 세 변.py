while True:
    angles = list(map(int, input().split()))
    #3개의 0이 입력되면 종료
    if angles.count(0) == 3:
        break

    angles.sort()
    #삼각형의 조건을 만족하지 못하는 경우
    if angles[0] + angles[1] <= angles[2]:
        print("Invalid")
    else:
        #정삼각형인 경우
        if len(set(angles)) == 1:
            print("Equilateral")
        #이등변삼각형인 경우
        elif len(set(angles)) == 2:
            print("Isosceles")
        else:
            print("Scalene")
            