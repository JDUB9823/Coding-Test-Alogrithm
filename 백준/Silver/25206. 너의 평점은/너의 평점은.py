transcript = []
getGrade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

while True:
    try:
        grade = list(input().split(" "))
        transcript.append(grade)
    except EOFError:
        break
        
totalCredit = 0
totalGrade = 0.0
for course, credit, grade in transcript:
    #P등급이 아닌 학점만 계산
    if grade != 'P':
        #총 학점에 해당 과목 학점 추가
        totalCredit += int(credit[0])
        #총 학점에 해당 과목 평점 추가, 과목평점 = 학점 * 등급
        totalGrade += int(credit[:1]) * getGrade[grade]

#format로 소수점 6번째 자리까지 출력
print(format(totalGrade/totalCredit, ".6f"))