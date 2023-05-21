n = int(input())
nums = list(map(int, input().split()))

last_num = None
for i in range(len(nums)):
    left = (nums[0])
    right = (nums[-1])
    if last_num is None:
        if left < right:
            last_num = left
            print('L', end='')
            nums.pop(0)
            continue
        else:
            last_num = right
            print('R', end='')
            nums.pop(-1)
            continue
    if last_num < left and last_num < right:
        if left < right and last_num < left:
            last_num = left
            print('L', end='')
            nums.pop(0)
            continue
        elif right < left and last_num < right:
            last_num = right
            print('R', end='')
            nums.pop(-1)
            continue
    elif last_num < left or last_num < right:
        if left < right:
            last_num = right
            print('R', end='')
            nums.pop(-1)
        else:
            last_num = left
            print('L', end='')
            nums.pop(0)
    else:
        break
        
        
