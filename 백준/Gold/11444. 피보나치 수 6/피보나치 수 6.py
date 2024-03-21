def mul(row, col1, col2, matA, matB):
    res = [[0] * col2 for _ in range(row)]
    for i in range(row):
        for j in range(col2):
            for k in range(col1):
                res[i][j] += matA[i][k] * matB[k][j] % 1000000007
    return res

def power(n, mat):
    if n == 1:
        return mat

    temp = power(n//2, mat)
    if n % 2 == 0:
        return mul(2, 2, 2, temp, temp)
    else:
        return mul(2, 2, 2, mat, mul(2, 2, 2, temp, temp))

n = int(input())
A = [[1,1], [1,0]]

if n < 3:
    print(1)
else:
    res = mul(2, 2, 1, power(n-1, A), [[1], [0]])
    print(*res[0])