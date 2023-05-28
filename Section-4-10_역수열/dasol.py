import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    n = int(input())
    nums = list(map(int, input().split()))
    answer = []
    visit = [1]*n

    def get_num():
        target = len(answer)  # 후보가 될수 있는 값
        for i in range(n):
            if nums[i] <= target:

                if target:
                    cnt = 0
                    for j in range(len(answer)):
                        if answer[j] > i + 1:
                            cnt += 1
                        if cnt == nums[i] and visit[i]:
                            visit[i] = 0
                            answer.append(i+1)
                            return
                else:
                    visit[i] = 0
                    answer.append(i+1)
                    return
    while len(answer) < n:
        get_num()
    # print(answer)
    sys.stdin = open(f'out{tc}.txt', 'rt')
    solution = list(map(int, input().split()))
    print(answer == solution)
