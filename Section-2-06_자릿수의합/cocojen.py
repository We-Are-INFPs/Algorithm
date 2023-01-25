n = int(input())


def digit_sum(x):
    my_sum = 0
    while x != 0:
        # 1의 자릿수 값을 얻기 위해 10으로 나눈 나머지를 구함
        digit = x % 10
        # my_sum 에 1의 자릿수 더해주고,
        my_sum += digit
        # 1의 자리는 이제 필요없으니까 10을 나눔
        x = x // 10
    return my_sum


max_sum = 0
answer = 0
nums = map(int, input().split())
for num in nums:
    ans = digit_sum(num)
    if ans > max_sum:
        max_sum = ans
        answer = num

print(answer)
