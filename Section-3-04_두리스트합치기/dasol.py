import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N = int(input())
    fir = list(map(int, input().split()))
    M = int(input())
    sec = list(map(int, input().split()))
    p1 = 0
    p2 = 0
    answer = []
    l1 = len(fir)
    l2 = len(sec)
    while 1:
        if fir[p1] <= sec[p2]:
            answer.append(fir[p1])
            p1 += 1
        elif fir[p1] >= sec[p2]:
            answer.append(sec[p2])
            p2 += 1
        if p1 >= l1:
            answer += sec[p2:]

            break
        if p2 >= l2:
            answer += fir[p1:]
            break
    # print(answer)
    # print(result)
    sys.stdin = open(f'out{tc}.txt', 'rt')
    result = list(map(int, input().split()))
    print('RIGHT?', answer == result)
