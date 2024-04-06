import sys
input = sys.stdin.readline

n = int(input())
stack, res = [], 0

for _ in range(n):
    height = int(input())

    #stack의 키가 현재 키보다 작은 경우 현재 사람이 볼 수 있는 pair 추가
    #stack을 항상 내림차순으로 유지
    while stack and stack[-1][0] < height:
        res += stack.pop()[1]

    #stack이 빈 경우, 현재 키 stack에 추가
    if not stack:
        stack.append([height, 1])
        continue

    #stack의 키가 현재 키보다 큰 경우, 현재 키 stack에 추가
    if stack[-1][0] > height:
        stack.append([height, 1])
        res += 1

    #stack의 키와 현재 키가 같은 경우, 기존의 count를 결과에 추가
    elif stack[-1][0] == height:
        prevCount = stack.pop()[1]
        res += prevCount

        #만약 stack이 비어있지 않다면, 현재 사람이 볼 수 있는 pair가 존재, 결과 + 1
        if stack:
            res += 1
        #현재 키와 기존 count + 1의 값 stack에 추가
        stack.append([height, prevCount + 1])

print(res)