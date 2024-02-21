def convertBase(number, base):
    division, remainder = divmod(number, base)
    return convertBase(division, base) + baseCode[remainder] if division else baseCode[remainder]

baseCode = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())
print(convertBase(N,B))