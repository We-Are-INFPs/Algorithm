n, m = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()

cnt = 0

while weights:
    if len(weights) == 1:
        cnt += 1
        break
    if weights[0] + weights[-1] >= m:
        cnt += 1
        weights.pop(0)
        weights.pop(0)
    else:
        cnt += 1
        weights.pop(0)

print(cnt)