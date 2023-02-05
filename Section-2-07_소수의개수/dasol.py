import sys
for t in range(1, 6):
    sys.stdin = open(f'in{t}.txt', 'rt')
    N = int(input())
    v = [True, True] + [False]*(N-1)
    for i in range(2, round(N/2)):
        if not v[i]:
            for j in range(i*2, N+1, i):
                if not v[j] and not j % i:
                    v[j] = True
    answer = 0
    for l in v:
        if not l:
            answer += 1
    print(answer)
