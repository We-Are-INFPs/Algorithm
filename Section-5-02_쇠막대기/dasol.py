import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    bars = input()
    laser = False
    stack = []
    n = 0
    for i in range(len(bars)):
        if bars[i] == '(':
            stack.append('(')
            laser = False
        elif bars[i] == ')' and laser:
            n += 1
            stack.pop(-1)
            laser = True
        else:
            stack.pop(-1)
            n += len(stack)
            laser = True
    print(n)
