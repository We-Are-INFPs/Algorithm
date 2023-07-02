import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    n = int(input())
    arr = list(range(1, n+1))
    for i in range(1 << len(arr)):
        subset = []
        for j in range(len(arr)):
            if i & (1 << j):
                subset.append(arr[j])
        print(subset)
    print('-----------------')
