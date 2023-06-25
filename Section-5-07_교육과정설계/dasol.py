import sys
from collections import deque
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    need = input()
    n = int(input())
    for i in range(n):
        plan = input()
        dq = deque(need)
        for x in plan:
            if x in dq:
                if x != dq.popleft():
                    print(f'#{i+1}, NO')
                    break
        else:
            if len(dq) == 0:
                print(f'#{i+1}, YES')
            else:
                print(f'#{i+1}, NO')
