n = int(input())

cnt: int = 0

sosus = [0] * (n+1)

for i in range(2, n+1):
    if sosus[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            sosus[j] = 1

print(cnt)