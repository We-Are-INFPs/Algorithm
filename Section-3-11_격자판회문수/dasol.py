from re import L
import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    arr = [list(map(int, input().split())) for _ in range(7)]
    result = 0
    for i in range(0, 3):
        for j in range(7):
            row = True
            col = True
            for l in range(3):
                if arr[i+l][j] != arr[i+4 - l][j]:
                    row = False
                if arr[j][i+l] != arr[j][i+4-l]:
                    col = False
            if row:
                result += 1
            if col:
                result += 1
    sys.stdin = open(f'out{tc}.txt', 'rt')
    answer = int(input())
    print('answer?', result == answer)
