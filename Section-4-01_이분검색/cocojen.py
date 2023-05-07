n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

start_idx = 0
end_idx = n-1


while start_idx <= end_idx:
    mid_idx = (start_idx + end_idx) // 2
    if nums[mid_idx] == m:
        print(mid_idx + 1)
        break
    elif nums[mid_idx] > m:
        end_idx = mid_idx - 1
    elif nums[mid_idx] < m:
        start_idx = mid_idx + 1
