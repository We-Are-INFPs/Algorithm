n = int(input())

scores = list(map(int, input().split()))

avg = round(sum(scores) / len(scores))

nearest_diff, nearest_score, std_idx = 9999999999, -999999999, 9999999999
for i in range(len(scores)):
    diff = scores[i] - avg
    if abs(diff) <= nearest_diff:
        temp_nearest_score = scores[i]
        temp_diff = abs(diff)
        temp_std_idx = std_idx
        if temp_diff == nearest_diff:
            if temp_nearest_score > nearest_score:
                nearest_score = temp_nearest_score
                std_idx = i
            elif i < temp_std_idx:
                std_idx = i
        else:
            nearest_diff = temp_diff
            nearest_score = temp_nearest_score
            std_idx = i
            
print(avg, std_idx+1)