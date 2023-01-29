def reverse(x) -> int:
    x = str(x)
    x = x.lstrip('0')  # remove leading zeroes
    return int(x[::-1])  # reverse and convert back to int


def isPrime(x) -> bool:
    if x == 1:
        return False
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


N = int(input())
nums = list(map(int, input().split()))

for x in nums:
    reversed_num = reverse(x)
    if isPrime(reversed_num):
        print(reversed_num, end=' ')
