import sys
for n in range(1, 6):
    sys.stdin = open(f'in{n}.txt', 'rt')
    N, K = map(int, input().split())
    cards = list(map(int, input().split()))
    nums = []
    for i in range(len(cards)):
        for j in range(len(cards)):
            for l in range(len(cards)):
                if i != j and j != l and i != l:
                    nums.append(cards[i] + cards[j]+cards[l])

    sortedArr = sorted(list(set(nums)), reverse=True)
    print(sortedArr[K-1])
