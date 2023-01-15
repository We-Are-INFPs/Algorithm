import sys
for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', 'rt')
    T = int(input())
    for j in range(T):
        N, s, e, k = map(int, input().split())
        nums = list(map(int, input().split()))
        part = sorted(nums[s-1:e])
        print(f'#{j+1} {part[k-1]}')
    print('---------------')
