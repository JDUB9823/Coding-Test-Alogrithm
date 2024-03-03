import sys

while True:
    string = sys.stdin.readline().rstrip()
    stack = []

    if string == ".":
        break

    for ch in string:
        if ch == "(":
            stack.append(ch)
        elif ch == "[":
            stack.append(ch)
        elif ch == ")":
            if not stack or stack[-1] != "(":
                print("no")
                break
            else:
                stack.pop()
        elif ch == "]":
            if not stack or stack[-1] != "[":
                print("no")
                break
            else:
                stack.pop()
    else: #for문에서 break를 하지 않고 수행이 종료된 경우
        if not stack:
            print("yes")
        else:
            print("no")