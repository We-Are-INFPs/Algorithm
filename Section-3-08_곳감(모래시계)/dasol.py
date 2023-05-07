import sys

for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    order = [list(map(int, input().split())) for _ in range(M)]
    for ord in order:
        rotate = ord[1]
        row = arr[ord[0]-1]

        m = ord[2] % N
        rotated_row = []
        if rotate:
            rotated_row = row[N-m:N] + row[:N-m]
        else:
            rotated_row = row[m:N] + row[:m]

        arr[ord[0]-1] = rotated_row
    gotgam = 0
    for i in range(N):
        for j in range(N):
            if min(i, N-i-1) <= j <= max(i, N-i-1):
                gotgam += arr[i][j]
    sys.stdin = open(f'out{tc}.txt', 'rt')
    answer = int(input())
    print('answer?', answer == gotgam)
