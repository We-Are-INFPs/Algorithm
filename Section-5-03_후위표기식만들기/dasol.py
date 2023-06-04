import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    text = input()
    answer = ''
    s = []
    order = {'*': 3, '/': 3, '+': 2, '-': 2}

    for i in text:
        if i.isdecimal():
            answer += i
        else:
            if i == '(':
                s.append(i)
            elif i == '*' or i == '/':
                while s and (s[-1] == '*' or s[-1] == '/'):
                    answer += s.pop()
                s.append(i)
            elif i == '+' or i == '-':
                while s and s[-1] != '(':
                    answer += s.pop()
                s.append(i)
            elif i == ')':
                while s and s[-1] != '(':
                    answer += s.pop()
                s.pop()  # ( 제거
    if len(s):
        answer += s.pop()
    print(answer)
