angles = list(map(int, input().split()))
angles.sort()

#삼각형의 조건 = 가장 긴 변이 나머지 두 변의 합보다 작다
condition = angles[0] + angles[1]
if condition <= angles[2]:
    print(condition + condition - 1)
else:
    print(sum(angles))
        