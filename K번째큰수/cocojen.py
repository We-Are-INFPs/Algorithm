n, nth = map(int, input().split())

nums = list(map(int, input().split()))

sums = []

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            sums.append(nums[i] + nums[j] + nums[k])
        
sums.sort(reverse=True)

answer = 0
cnt = 0
for sum_num in sums:
    if sum_num != answer:
        answer = sum_num
        cnt += 1
    if cnt == nth:
        print(answer)
        break
