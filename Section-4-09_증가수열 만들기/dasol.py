import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    n = int(input())
    nums = list(map(int, input().split()))
    answer = ''
    l = 0
    r = n - 1
    c = 0
    while 1:
        if r < l:
            break
        if c < nums[l] < nums[r] or nums[r] < c < nums[l]:
            answer += 'L'
            c = nums[l]
            l += 1
        elif c < nums[r] < nums[l] or nums[l] < c < nums[r]:
            answer += 'R'
            c = nums[r]
            r -= 1
        else:
            break
    print('answer', answer)
