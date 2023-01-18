import sys
for t in range(1, 6):
    sys.stdin = open(f'in{t}.txt', 'rt')
    N, M = map(int, input().split())
    ans = []
    maxNum = max(N, M)
    for i in range(abs(N-M), -1, -1):
        ans.append(maxNum -i +1)
    print(ans)
#    1 => 2, 3, 4, 5, 6, 7, 8
#    2 => 3, 4, 5, 6, 7, 8, 9
#    3 => 4, 5, 6, 7, 8, 9, 10
#    4 => 5, 6, 7, 8, 9, 10, 11

#    5 => 6, 7, 8, 9, 10, 11, 12
#    6 => 7, 8, 9, 10, 11, 12, 13
    
# cnt = n- m +1  = 4
# 7, 4 => 8, 7, 6, 5