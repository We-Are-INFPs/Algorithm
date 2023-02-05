import sys
for t in range(1, 6):
    sys.stdin = open(f'in{t}.txt', 'rt')
    N = int(input())
    ans = 0
    for k in range(N):
        nums = list(map(int, input().split()))
        nums.sort()
        repetitive_num = 0
        max_num = 0
        repeat_cnt = 0
        total = 10
        for i in range(len(nums)):
            if not i:
                max_num = nums[i]
                continue
            if nums[i] == nums[i-1]:
                repetitive_num = nums[i]
                repeat_cnt += 1
            if nums[i] > max_num:
                max_num = nums[i]

        if repeat_cnt:

            total += repetitive_num
            total *= (10 ** (repeat_cnt+1))
        else:
            total *= (10 * max_num)

        if total > ans:
            ans = total
    print(ans)
