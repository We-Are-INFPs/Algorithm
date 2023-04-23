import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    cards = [i for i in range(21)]
    for j in range(10):
        s, e = map(int, input().split())
        cards = cards[:s] + cards[s:e+1:][::-1] + cards[e+1:]
    print(*cards[1:], sep=' ')

    # 정답을 채점해보자~!
    sys.stdin = open(f'out{tc}.txt', 'rt')
    answer = list(map(int, input().split()))
    print('isRight?', answer == cards[1:])
