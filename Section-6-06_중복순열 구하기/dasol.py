import sys
from itertools import product
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    n, m = map(int, input().split())

    arr = [i for i in range(1, n+1)]
    answer = list(product(arr, repeat=m))
    for i in answer:
        print(*i)
    print(len(answer))
