import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    lt = 1
    rt = sum(arr)
    res = 0

    def count(x):
        cnt = 1
        sum = 0
        for i in arr:
            if sum + i > x:
                cnt += 1
                sum = i
            else:
                sum += i
        return cnt

    while lt <= rt:

        mid = (lt + rt) // 2
        if count(mid) <= M:
            res = mid
            rt = mid - 1
        else:
            lt = mid + 1
    print(res)
