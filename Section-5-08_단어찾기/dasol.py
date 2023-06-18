import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    n = int(input())
    arr = []
    while True:
        try:
            line = input()
            arr.append(line)
        except EOFError:
            break
    count = {}
    for i in range(len(arr)):
        word = arr[i]
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    answer = ''
    for key, value in count.items():
        if value == 1:
            answer = key
    print(answer)
