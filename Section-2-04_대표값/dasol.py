import sys
for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', 'rt')
    N = int(input())
    scores = list(map(int, input().split()))
    # print(f'scores, {scores}')
    studentAvg = round(sum(scores) / N)
    studentIdx = -1
    studentScore = 0
    minGap = 1000000
    for j in range(N):
        gap = abs(scores[j] -studentAvg)
        if (gap < minGap):
            studentIdx = j
            studentScore = scores[j]
            minGap = gap
    print( studentAvg, studentIdx +1)
