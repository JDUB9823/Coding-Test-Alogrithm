num = list(map(int, input().split()))
v = 0

for n in num:
    v += n**2
print(v%10)