"""
10 1011100110


"""

n = int(input())
q = list(map(int, input().split()))

total_score = 0

in_row = 0

for i in range(n):
    if i == n-1 and q[i] == 1:
        for j in range(1, in_row+2):
            total_score += j
    if q[i] == 1:
        in_row += 1
    elif q[i] == 1 and i == n - 1:
        for j in range(1, in_row+1):
            total_score += j
    elif q[i] == 0:
        temp_score = 0
        for j in range(1, in_row+1):
            temp_score += j
        total_score += temp_score
        in_row = 0
    

print(total_score)
        
        