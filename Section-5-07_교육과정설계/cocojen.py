"""
while 순서 스택도에서 첫번째 엘리먼트를 pop함.
수업계획 스택에서 첫번째 엘리먼트를 만날때까지 계속 pop

"""
from collections import deque

order = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(order)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
