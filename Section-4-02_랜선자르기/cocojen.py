k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
start = 1
end = max(lines)

while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for line in lines:
        cnt += (line//mid)
    if cnt < n:
        # n이 더 크면 더 크게 나눠진거니까 자르는 길이를 줄인다
        end = mid - 1
    else:
        # n이 더 작으면 검색조건에 해당되게 잘 나눠진것이니까 일단 result 를 업데이트하고,
        # 더 크게 나눠볼 수 있는지 확인한다
        result = mid
        start = mid + 1

print(result)