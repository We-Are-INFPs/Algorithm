import sys
from itertools import combinations
for tc in range(0, 1):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    m, n = map(int, input().split())
    arr = [i for i in range(1, m+1)]
    cnt = 0
    for i in combinations(arr, n):
        cnt += 1
        print(*i, end="\n")
    print(cnt)
