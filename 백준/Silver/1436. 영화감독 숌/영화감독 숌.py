N = int(input())
number, count = 665, 0

while count < N:
    number += 1
    if str(number).find('666') != -1:
        count += 1
        
print(number)