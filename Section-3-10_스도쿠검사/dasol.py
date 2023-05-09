from re import L
import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    nums = {}
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum_total = sum(n)
    result = True
    for i in range(9):
        row = 0
        col = 0
        for j in range(9):
            row += sudoku[i][j]
            col += sudoku[j][i]
            if sudoku[i][j] in nums:
                nums[sudoku[i][j]] += 1
            else:
                nums[sudoku[i][j]] = 1
        if row != sum_total or col != sum_total:
            result = False
            break
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = 0
            for l in range(3):
                for m in range(3):
                    temp += sudoku[i+l][j+m]
            if temp != sum_total:
                result = False
                break
    for i in range(9):
        if nums[i+1] != 9:
            result = False
    sys.stdin = open(f'out{tc}.txt', 'rt')
    answer = input()
    my_ans = 'YES' if result else 'NO'
    print('answer?', my_ans == answer)
