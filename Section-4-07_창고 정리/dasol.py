import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    arr.sort()
    amount_low = 1

    def get_low():
        temp = M
        cnt = 1
        for l in range(1, len(arr)):
            if (arr[l] - arr[l-1]) * cnt == temp:
                return arr[l]
            elif (arr[l] - arr[l-1]) * cnt < temp:
                temp -= (arr[l] - arr[l-1]) * cnt
                cnt += 1
            else:
                return arr[l-1] + (temp // cnt)
    low = get_low()

    def get_high():
        temp = M
        cnt = 1
        for l in range(len(arr)-2, -1, -1):
            if (arr[l+1] - arr[l]) * cnt == temp:
                return arr[l+1]
            elif (arr[l+1] - arr[l]) * cnt < temp:
                temp -= (arr[l+1] - arr[l]) * cnt
                cnt += 1
            else:
                return arr[l+1] - (temp // cnt)
    high = get_high()
    print(high-low)
