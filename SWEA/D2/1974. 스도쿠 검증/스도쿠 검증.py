T = int(input())

for tc in range(1, T+1):
    sudoku = []

    for _ in range(9):
        sudoku.append(list(map(int, input().split())))

    flag = True
    for i in range(9):
        rowCheck = set(sudoku[i][:9])
        colCheck = set(sudoku[j][i] for j in range(9))
        if len(rowCheck) != 9 or len(colCheck) != 9:
            flag = False
            break

    for i in range(0, 9, 3):
        boxCheck = set()
        for j in range(i, i+3):
            boxCheck.add(sudoku[j][i])
            boxCheck.add(sudoku[j][i+1])
            boxCheck.add(sudoku[j][i+2])
        if len(boxCheck) != 9:
            flag = False
            break
    
    print(f"#{tc} 0" if flag == False else f"#{tc} 1")