import sys

for n in range(1, 6):
  sys.stdin = open(f'in{n}.txt', 'rt')
  N, K = map(int, input().split())
  arr = list(map(int, input().split()))
  size = len(arr)
  calSet = set()

  for i in range(size):
    for j in range(i+1, size):
      for m in range(j+1, size):
        calSet.add(arr[i] + arr[j] + arr[m])

  print (sorted(list(calSet), reverse=True)[K-1])