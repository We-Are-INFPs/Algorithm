from collections import deque

"""
첨에는 그러면 숫자 크기 순 아닌가 생각했음.
그런데 그렇게 하면 위험도가 같은 경우를 구할 수 없음.
그래서 큐를 써야함.
또 m번째 환자의 위험도로 해당 환자인지 체크하려니까 위험도가 같은 경우는 또 못 구함.
그래서 먼저 인덱스를 부여해주고 시작해야함.

1. 리스트에서 맨 왼쪽 element 를 꺼냄. pop()
2. 이 element 가 리스트에 있는 애들보다 큰지 확인함 -> any()
3. 크다면 m과 같은 값인지 continue.
4. 크지 않다면 리스트 오른쪽에 append() 하고, 1번부터 다시 반복
"""
n, m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break
"""
60 50 70 80 90
50 70 80 90 60
70 80 90 60 50
80 90 60 50 70
90 60 50 70 80 -> 90 진료
60 50 70 80
50 70 80 60
70 80 60 50
80 60 50 70 -> 80 진료
5 2
60 50 70 80 90
---
[60] 60 90 60 60 60
60 90 60 60 60 [60]
90 60 60 60 [60] 60 -> 90 진료
60 60 60 [60] 60 -> 진료
60 60 [60] 60 -> 진료
60 [60] 60 -> 진료
[60] 60 -> 진료
"""

