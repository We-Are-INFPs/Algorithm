import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    k, N = map(int, input().split())

    arr = [int(input()) for _ in range(k)]
    total = 0
    for a in arr:
        total += a
    num = total // N
    my_ans = 0

    def getMax(x):
        temp = 0
        for i in arr:
            temp += (i // x)
        return temp

    while 1:
        num -= 1
        temp_max = getMax(num)
        if temp_max >= N:
            my_ans = num
            break

    print(my_ans)
