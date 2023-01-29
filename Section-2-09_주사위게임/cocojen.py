

max_score: int = 0

def repeat_num(arr):
    repeat_dict = {}
    for num in arr:
        if num in repeat_dict:
            repeat_dict[num] += 1
        else:
            repeat_dict[num] = 1
    max_repeated_cnt = 0
    max_value_num = 0
    for num, repeated_num in repeat_dict.items():
        if repeated_num > max_repeated_cnt:
            max_repeated_cnt = repeated_num
            max_value_num = num
    if max_repeated_cnt == 3:
        return 10000 + (max_value_num)*1000
    elif max_repeated_cnt == 2:
        return 1000 + (max_value_num)*100
    elif max_repeated_cnt == 1:
        return max(arr) * 100


N: int = int(input())


max_answer = 0
for i in range(N):
    nums = list(map(int, input().split()))
    ans = repeat_num(nums)
    if max_answer < ans:
        max_answer = ans
        
print(max_answer)