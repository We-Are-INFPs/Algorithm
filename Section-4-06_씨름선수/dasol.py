import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N = int(input())
    app = [list(map(int, input().split())) for _ in range(N)]
    app.sort(key=lambda x: (x[0], x[1]))
    s = 0
    cnt = 0
    while s < N:
        for i in range(s+1, N):
            if app[s][1] <= app[i][1]:
                s = i
        else:
            cnt += 1
            s += 1
    print(cnt)
