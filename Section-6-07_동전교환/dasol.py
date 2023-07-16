import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    n = int(input())
    kind = list(map(int, input().split()))
    m = int(input())
    minC = m
    kind.sort(reverse=True)

    def dfs(l, sum):
        global minC
        if l > minC:
            return
        if sum > m:
            return
        if sum == m:
            if l < minC:
                minC = l
        else:
            for i in range(n):
                dfs(l+1, sum + kind[i])

    dfs(0, 0)
    print(minC)
