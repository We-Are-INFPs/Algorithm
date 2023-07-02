nums, m = map(int, input().split())
nums = list(map(int, str(nums)))

stack = []

for num in nums:
    while stack and m > 0 and stack[-1] < num:
        stack.pop()
        m -= 1
    stack.append(num)

if m != 0:
    stack = stack[:-m]
    
res = ''.join(map(str, stack))
print(res)