import sys


for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_total = 0

    def search():
        temp_row = 0
        temp_col = 0
        temp_dia1 = 0
        temp_dia2 = 0
        global max_total
        for i in range(N):
            for j in range(N):
                temp_row += arr[i][j]
                temp_col += arr[j][i]
                if i == j:
                    temp_dia1 += arr[i][j]
                if i + j == N-1:
                    temp_dia2 += arr[i][j]
            max_total = max(temp_row, temp_col, max_total,
                            temp_dia1, temp_dia2)
            temp_row = 0
            temp_col = 0
            temp_dia1 = 0
            temp_dia2 = 0
    search()
    sys.stdin = open(f'out{tc}.txt', 'rt')
    answer = int(input())
    print('is Right?', max_total == answer)
