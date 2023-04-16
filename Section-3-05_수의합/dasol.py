import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    result = 0
    i = 0

    while i < N:
        if arr[i] == M:
            i += 1
            result += 1
            continue
        temp = arr[i]
        j = i + 1
        while j < N:
            if temp + arr[j] < M:
                temp += arr[j]
                j += 1
                continue
            elif temp + arr[j] == M:
                result += 1
                break
            else:
                break
        i += 1
    print(result)
    sys.stdin = open(f'out{tc}.txt', 'rt')
    answer = int(input())
    print('Right?', result == answer)


# 10 5
# 3 2 2 1 3 1 2 3 2 2
