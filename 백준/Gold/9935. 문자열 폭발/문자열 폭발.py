import sys
input = sys.stdin.readline

stack = []
string = input().rstrip()
explosion = input().rstrip()

for s in string:
    stack.append(s)
    if ''.join(stack[-len(explosion):]) == explosion:
        del stack[-len(explosion):]

if stack:
    print(''.join(stack))
else:
    print("FRULA")