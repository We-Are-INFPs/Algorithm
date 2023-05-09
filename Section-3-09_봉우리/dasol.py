from re import L
import sys
from pprint import pprint


for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[1 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if j > 0:
                if arr[i][j] <= arr[i][j-1]:
                    visit[i][j] = 0
                if arr[i][j] >= arr[i][j-1]:
                    visit[i][j-1] = 0
                if arr[j][i] <= arr[j-1][i]:
                    visit[j][i] = 0
                if arr[j][i] >= arr[j-1][i]:
                    visit[j-1][i] = 0
    total = 0
    for m in range(N):
        for n in range(N):
            if visit[m][n]:
                total += 1
    sys.stdin = open(f'out{tc}.txt', 'rt')
    answer = int(input())
    print('answer?', total == answer)
