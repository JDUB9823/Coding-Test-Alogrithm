import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    minCost = [[0] * k for _ in range(k)] #DP

    #파일의 누적 합
    PS = {-1 : 0}
    for i in range(k):
        PS[i] = PS[i-1] + files[i]

    #sumSize는 sumSize만큼의 파일들의 합
    #sumSize = 2일 경우 파일 2개의 합을 구함
    for sumSize in range(1, k):
        for start in range(k-1):
            end = start + sumSize
            if end >= len(files):
                break
                
            #파일의 크기 최대 값
            res = sys.maxsize
            #sumSize가 3이고 start가 3, end가 6이라고 가정하여 minCost[3][6]을 2개로 분할
            #minCost[3][3] + minCost[4][6], minCost[3][4] + minCost[5][6], minCost[3][5] + minCost[6][6]으로 분할됨
            #위 3개 분할 중 첫번째가 최소 비용이라고 가정, 결과는 분할 값 + 누적합 값
            #files[3]부터 [6]까지의 누적 합은 PS[6] - PS[3 - 1]
            for cur in range(start, end):
                res = min(res, minCost[start][cur] + minCost[cur+1][end] + PS[end] - PS[start - 1])
            minCost[start][end] = res

    print(minCost[0][-1])