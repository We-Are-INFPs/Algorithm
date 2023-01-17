import sys
sys.stdin = open("./k번째약수.txt",'r')

N, K = map(int, input().split())

arr = []
for i in range(1, N + 1):
    if N % i == 0: # 약수면 추가
        arr.append(i)

if K > len(arr): # 약수 모음 개수가 더 작은 경우
    print(0)
else:
    print(arr[K-1])

# 파이썬 적응안된다 ... 예전엔 파이썬이 제일 쉽다고 생각했는데 ...
