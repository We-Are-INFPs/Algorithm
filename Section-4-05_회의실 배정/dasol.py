import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N = int(input())
    mt = [list(map(int, (input().split()))) for _ in range(N)]
    mt.sort(key=lambda x: (x[1], x[0]))

    cnt = 1
    end = mt[0][1]
    for i in range(1, N):
        if mt[i][0] >= end:
            cnt += 1
            end = mt[i][1]

    print(cnt)
