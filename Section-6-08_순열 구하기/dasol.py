import sys
from itertools import permutations
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    n, m = map(int, input().split())
    arr = [i for i in range(1, n+1)]
    cnt = 0
    for i in permutations(arr, m):
        cnt += 1
        print(*i, end="\n")
    print(cnt)

    # visit = [False]*n

    # for j in range(n):
    #     t = 0
    #     comb = [j+1]
    #     while t < m:
    #         for i in range(n):
    #             if not visit[i]:
    #                 comb.append(i+1)
    #             if len(comb) == m:
    #                 break

    #         t += 1
    #         if t == m:
    #             print(*comb)
    #             comb = [j+1]
    #             print()
    #             visit = [False]*n
