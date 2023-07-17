import heapq as hq

a=[]

while True:
    n=int(input())
    #프로그램 종료
    if n==-1:
        break
    #최소값 출력
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a))
    #최소힙에 자료 입력
    else:
        hq.heappush(a, n)