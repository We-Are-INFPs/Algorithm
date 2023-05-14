import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N, C = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    lt = 1
    arr.sort()
    rt = arr[-1]
    res = 0

    def count(len):
        cnt = 1
        ep = arr[0]  # end point
        for i in range(1, N):
            if arr[i] - ep >= len:  # 마지막에 말을 배치한 지점이 len보다 크면
                cnt += 1
                ep = arr[i]
        return cnt  # 배치한 말의 개수 리턴

    while lt <= rt:
        mid = (lt + rt) // 2
        if count(mid) >= C:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1
    print(res)
