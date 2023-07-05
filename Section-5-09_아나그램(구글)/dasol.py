import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    foo = input()
    bar = input()
    fooCom = {}
    barCom = {}
    for i in range(len(foo)):
        f = foo[i].lower()
        b = bar[i].lower()
        if f in fooCom:
            fooCom[f] += 1
        else:
            fooCom[f] = 1
        if b in barCom:
            barCom[b] += 1
        else:
            barCom[b] = 1
    answer = 'YES'
    for key, value in fooCom.items():
        if barCom[key] != value:
            answer = 'NO'
            break
    print(answer)
