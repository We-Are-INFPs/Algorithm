n = int(input())

candidates = []
cnt = 0

for i in range(n):
    height, weight = map(int, input().split())
    candidates.append((height, weight))
    
# 키순정렬
candidates.sort(reverse=True)

max_weight = 0

for height, weight in candidates:
    if weight > max_weight:
        cnt += 1
        max_weight = weight
        
print(cnt)
