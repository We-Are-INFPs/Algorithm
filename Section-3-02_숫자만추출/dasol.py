import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    word = input()
    res = ''
    for i in word:
        if i.isdigit():
            res += i
    res = int(res)
    divisor = 0
    for j in range(1, res+1):
        if not res % j:
            divisor += 1
    print(res)
    print(divisor)
