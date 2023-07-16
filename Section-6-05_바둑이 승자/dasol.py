import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    c, n = map(int, input().split())
    weights = [int(input()) for _ in range(n)]
    maxSum = 0

    def dfs(i, s):
        global maxSum
        if s + weights[i] > c:
            return
        if s + weights[i] > maxSum:
            maxSum = s + weights[i]

        if i+1 < n:
            dfs(i+1, s + weights[i])
            dfs(i+1, s)
    dfs(0, 0)
    print(maxSum)
