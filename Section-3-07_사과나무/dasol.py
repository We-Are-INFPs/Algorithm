import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mid = N // 2
    total = 0
    for i in range(N):
        for j in range(N):
            if abs(mid-j) <= min(i, N-i-1):
                total += arr[i][j]
    sys.stdin = open(f'out{tc}.txt', 'rt')
    answer = int(input())
    print('정답인가요?', answer == total)
