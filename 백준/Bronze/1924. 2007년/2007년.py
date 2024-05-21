x, y = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(x - 1):
    y += month[i]

day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

print(day[(y%7)])