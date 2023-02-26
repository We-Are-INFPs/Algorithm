import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N = int(input())
    scores = list(map(int, input().split()))
    ans = 0
    prev = 0
    for i in range(len(scores)):
        if scores[i]:
            prev += 1
            ans += prev
        else:
            prev = 0
    print(ans)
