import sys

N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
#스택 = 간식받는 줄과 기다리는 줄 사이의 1열공간
stack = []
order = 1

while order <= N:
    #기다리는 줄 맨 앞이 간식 받는 순서인 경우
    if line and line[0] == order:
        line.pop(0)
        order += 1
    elif stack and stack[-1] == order:
        while stack:
            #스택의 맨 마지막에 들어간 사람이 간식을 받는 순서가 아닌 경우
            if stack[-1] != order:
                break
            #스택의 맨 마지막에 들어간 사람이 간식을 받는 순서인 경우
            else:
                stack.pop()
                order += 1
    #기다리는 줄의 맨 앞이 간식을 받는 순서가 아닌 경우
    elif line:
        stack.append(line[0])
        line.pop(0)

    #기다리는 사람이 없고 스택의 간식 받는 순서가 엉망인 경우
    if not line and stack and stack[-1] != order:
        break

if not stack and not line:
    print("Nice")
else:
    print("Sad")