import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    n = int(input())
    arr = list(map(int, input().split()))
    arrSum = 0
    for a in range(len(arr)):
        arrSum += arr[a]
    if arrSum % 2:
        print('NO')
    else:
        for i in range(1 << len(arr)):
            temp = 0
            for j in range(len(arr)):
                if i & (1 << j):
                    temp += arr[j]
            if temp * 2 == arrSum:
                print('YES')
                break
        else:
            print('NO')
