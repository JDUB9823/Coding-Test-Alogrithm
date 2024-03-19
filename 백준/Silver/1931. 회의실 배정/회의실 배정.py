import sys
input = sys.stdin.readline

n = int(input())
rooms = [list(map(int, input().split())) for _ in range(n)]
rooms.sort(key = lambda x : (x[1], x[0]))
count, time = 0, 0

for room in rooms:
    if time <= room[0]:
        time = room[1]
        count += 1

print(count)