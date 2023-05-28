import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.sort()
    low = 0
    high = len(weights)-1
    cnt = 0
    while low <= high:
        if weights[low] + weights[high] <= m:
            low += 1
            high -= 1
            cnt += 1
        else:
            high -= 1
            cnt += 1
    print(cnt)
