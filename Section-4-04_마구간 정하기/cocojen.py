from itertools import combinations

n, c = map(int, input().split())

locations = [int(input()) for _ in range(n)]

locations.sort()

lt = locations[0]
rt = locations[-1]

res = 0


def count_func(len):
    cnt = 1
    ep = locations[0]
    for i in range(1, n):
        if locations[i] - ep >= len:
            cnt += 1
            ep = locations[i]
    return cnt


while lt <= rt:
    mid = (lt + rt) // 2
    if count_func(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
