import sys

N, M = map(int, sys.stdin.readline().split())
numDict, nameDict = {}, {}

for i in range(1, N+1):
    pokemon = sys.stdin.readline().rstrip()
    numDict[i] = pokemon
    nameDict[pokemon] = i

for _ in range(M):
    Q = sys.stdin.readline().rstrip()
    if Q.isdecimal():
        print(numDict[int(Q)])
    elif Q.isalpha():
        print(nameDict[Q])