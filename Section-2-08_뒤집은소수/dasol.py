import sys
for t in range(1, 6):
    sys.stdin = open(f'in{t}.txt', 'rt')
    N = int(input())
    nums = list(map(int, input().split()))
    ans = []

    def isPrime(x):
        if x < 2:
            return False
        prime = True
        for i in range(2, round(x)):
            if not x % i:
                prime = False
                break
        return prime

    def reverse(x):
        return int("".join(list(str(x))[::-1]))
    for n in nums:
        reversed_n = reverse(n)
        if isPrime(reversed_n):
            ans.append(reversed_n)
    print(*ans, sep=" ")
