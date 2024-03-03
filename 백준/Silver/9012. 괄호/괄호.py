import sys

N = int(sys.stdin.readline())

for _ in range(N):
    stack = []
    string = sys.stdin.readline().rstrip()

    for ch in string:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                print("NO")
                break
            else:
                stack.pop()
    else: #for문에서 break를 안했을 경우
        if not stack:
            print("YES")
        else:
            print("NO")