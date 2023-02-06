import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    N = int(input())
    for n in range(N):
        ans = True
        word = input()
        for i in range(round(len(word)/2)):
            if word[i].lower() != word[len(word) - 1 - i].lower():
                ans = False
                break
        print(f'#{n+1}', 'YES' if ans else 'NO')
