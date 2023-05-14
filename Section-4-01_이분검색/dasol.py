import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    sta = 0
    end = N-1
    mid = N // 2
    my_answer = 1
    while 1:
        if M == arr[mid]:
            my_answer += mid
            break
        elif M > arr[mid]:
            sta = mid + 1
            mid = (sta + end + 1) // 2
        else:
            end = mid - 1
            mid = (sta + end + 1) // 2
    print(my_answer)
