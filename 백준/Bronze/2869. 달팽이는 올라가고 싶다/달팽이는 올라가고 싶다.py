A, B, V = map(int, input().split())

#달팽이가 V위치에 도착하는 날 = days
#V = A*days - B*(days-1) => days = (V-B) / (A-B)
days = (V-B) / (A-B)

#days가 정수이면? V위치 도착, 소수이면? 다음날에 V위치 도착
print(int(days) if int(days) == days else int(days) + 1)