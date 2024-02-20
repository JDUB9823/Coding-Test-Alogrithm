N = int(input())
divisor = 2

while N > 1:
    if N % divisor == 0:
        print(divisor)
        N = N // divisor
    else:
        divisor += 1