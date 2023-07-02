import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N = int(input())
    nums = list(map(int, input().split()))

    def can_partition(nums):
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return "NO"

        target_sum = total_sum // 2
        dp = [False] * (target_sum + 1)
        dp[0] = True
        for num in nums:
            for i in range(target_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        if dp[target_sum]:
            return "YES"
        else:
            return "NO"

    print(can_partition(nums))

