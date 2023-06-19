n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

meetings = []

for i in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

### 끝나는시간으로 정렬하는 것이 포인트
meetings.sort(key=lambda x: (x[1], x[0]))

end_at = 0
cnt = 0

for start, end in meetings:
    if start >= end_at:
        end_at = end
        cnt += 1

print(cnt)
