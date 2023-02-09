n = int(input())

for i in range(n):
    chars = input().upper()
    if chars == chars[::-1]:
        print(f'#{i+1} YES')
    else:
        print(f'#{i+1} NO')