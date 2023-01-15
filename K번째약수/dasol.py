import sys
sys.stdin = open('in5.txt', 'rt')
N, K = map(int, input().split())

yak = []

for i in range(1, N // 2):
    if not N % i:
        yak.append(i)
        if i != round(N/i):
            yak.append(round(N/i))

yak = list(set(yak))
yak.sort()
if len(yak) >= K:
    print(yak[K-1])
else:
    print(-1)
