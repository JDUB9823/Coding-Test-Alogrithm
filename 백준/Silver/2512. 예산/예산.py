n = int(input())
budgets = list(map(int, input().split()))
limit = int(input())

if sum(budgets) <= limit:
    print(max(budgets))
else:
    start, end = 1, limit
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for budget in budgets:
            total += budget if budget <= mid else mid

        if total <= limit:
            start = mid + 1
        else:
            end = mid - 1
    print(end)