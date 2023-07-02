import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    n, m = map(int, input().split())
    N = str(n)

    def remove_index(num):
        for i in range(len(num)-1):
            if num[i] < num[i+1]:
                return i
        else:
            return len(num)-1

    while m:
        idx = remove_index(N)
        N = N[:idx] + N[idx+1:]
        m -= 1
    print(N)
