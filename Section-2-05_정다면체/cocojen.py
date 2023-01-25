n, m = map(int, input().split())

sums = []

# 나올 수 있는 모든 합을 sums 에 담는다
for i in range(1, n+1):
    for j in range(1, m+1):
        sums.append(i+j)
        
answers = [0] * (n*m)

# 얼마나 반복되는지 세기위해 같은 index 에 1씩 더한다
for sum in sums:
    answers[sum] += 1

cnt = 0
# 가장 많이 반복된 횟수를 찾는다
max_num = max(answers)

results = []
for i in range(len(answers)):
    # 가장 많이 반복된 값이면 인덱스를 result 에 넣는다
    if answers[i] == max_num:
        results.append(i)
        
print(*sorted(results), sep=" ")
