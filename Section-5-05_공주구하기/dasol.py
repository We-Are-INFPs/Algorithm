import sys
from collections import deque
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    n, k = map(int, input().split())
    dq = list(range(1, n+1))
    dq = deque(dq)
    while dq:
        for _ in range(k-1):
            cur = dq.popleft()
            dq.append(cur)
        dq.popleft()
        if len(dq) == 1:
            print(dq[0])

    # 나의풀이
    # arr = [True]*n
    # i = 0
    # p = 0
    # cnt = 0
    # while i < n-1:
    #     if arr[p % n]:
    #         cnt += 1
    #     if cnt == 3:
    #         arr[p % n] = False
    #         i += 1
    #         cnt = 0
    #     p += 1
    # ans = -1

    # for j in range(len(arr)):
    #     if arr[j]:
    #         ans = j + 1
    # print(ans)
