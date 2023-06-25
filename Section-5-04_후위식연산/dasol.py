from contextlib import nullcontext
import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    ex = input()
    left = None
    right = None
    stack = []

    def calculate(a, b, op):
        a = int(a)
        b = int(b)
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a*b
        if op == '/':
            return a/b
    for x in ex:
        if x.isdecimal():
            stack.append(x)
        else:
            temp2 = stack.pop()
            temp1 = stack.pop()
            temp3 = calculate(temp1, temp2, x)
            stack.append(temp3)
    print(*stack)
