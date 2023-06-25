import sys
import heapq as hq
for tc in range(1, 2):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    a = []
    answer = []

    while True:
        try:
            line = int(input())
            if line < 0:
                break
            if line == 0:
                if len(a) == 0:
                    print(-1)
                else:
                    print(-hq.heappop(a))
            else:
                hq.heappush(a, -line)
        except EOFError:
            break
    print('-----------------------------')
