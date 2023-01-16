import sys
sys.stdin = open("./k번째수.txt",'r')

T = int(input())
for tc in range(T):
  N, s, e, k = map(int, input().split())
  arr = list(map(int, input().split()))
  # s부터 e까지 오름차순 정렬 후 k번째 숫자 출력
  result = sorted(arr[s-1:e])[k-1]
  print(result)