import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    answer = ''

    n = int(input())

    def jinsu(x):
        global answer
        quotient = x // 2
        remainder = x % 2
        answer = str(remainder) + answer
        if quotient >= 2:
            jinsu(quotient)
        elif quotient > 0:
            answer = str(quotient) + answer
            return
        else:
            return
    jinsu(n)
    print(answer)
