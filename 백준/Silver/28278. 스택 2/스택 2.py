import sys

N = int(sys.stdin.readline())
stack = [] #스택 = LIFO

for _ in range(N):
    command = sys.stdin.readline().rstrip()

    if command[0] == "1":
        stack.append(int(command.split()[1]))
    elif command[0] == "2":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif command[0] == "3":
        print(len(stack))
    elif command[0] == "4":
        print(1 if not stack else 0)
    elif command[0] == "5":
        print(-1 if not stack else stack[-1])