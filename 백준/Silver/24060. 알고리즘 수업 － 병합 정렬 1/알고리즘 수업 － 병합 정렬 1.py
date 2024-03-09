import sys

def merge_sort(A,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1, r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    global cnt, ans
    i = p
    j = q+1
    t = 1
    tmp = [0] * (r-p+2)
    while i<=q and j<=r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t+=1
            i+=1
        else:
            tmp[t] = A[j]
            t+=1
            j+=1
    #왼쪽 배열이 남은 경우
    while i<=q:
        tmp[t] = A[i]
        t+=1
        i+=1
    #오른쪽 배열이 남은 경우
    while j<=r:
        tmp[t] = A[j]
        t+=1
        j+=1
    #Merge 결과 저장
    i, t = p, 1
    while i<=r:
        A[i] = tmp[t]
        i += 1
        t += 1
        cnt += 1
        if cnt == K:
            ans = A[i-1]
            return

cnt, ans = 0, -1
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

merge_sort(arr,0,N-1)
print(ans)