def getFactors (N):
    return [factor for factor in range(1, N) if N % factor == 0]

while True:
    N = int(input())
    if N == -1:
        break
        
    factors = getFactors(N)
    if sum(factors) == N:
        print(f"{N} = {' + '.join(str(factor) for factor in factors)}")
    else:
        print(f"{N} is NOT perfect.")