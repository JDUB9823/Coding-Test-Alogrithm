N = list(map(int, input()))
N.sort(reverse=True)

for num in N:
    print(num, end="")