def Count(capacity):
    cnt = 1
    sum = 0
    for x in List:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


n, k = map(int, input().split())
List = list(map(int, input().split()))
res = 0
lt = 1
rt = sum(List)

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) <= k:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
