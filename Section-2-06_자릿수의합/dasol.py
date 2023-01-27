import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N = int(input())
    nums = list(map(int, input().split()))
    def digit_sum(x):
        summed_num = 0
        num = x
        while num:
            summed_num += num % 10
            num //=10
        return summed_num

    maxSum = 0
    maxN = 0
    for i in range(N):
        summed = digit_sum(nums[i])
        if (summed > maxSum):
            maxSum = summed
            maxN = nums[i]
        
    print(maxN)