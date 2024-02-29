import sys

N = int(sys.stdin.readline())
S = set()

for _ in range(N):
    name, log = sys.stdin.readline().split()
    if log == "enter":
        S.add(name)
    elif log == "leave":
        S.remove(name)

#사전 순의 역순으로 정렬
company = sorted(S, reverse=True)

for employee in company:
    print(employee)