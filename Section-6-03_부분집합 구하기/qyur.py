import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    number = int(input())

    def generate_subsets(n):
      def backtrack(start, subset):
          if subset:
            print(subset)

          for i in range(start, n+1):
              subset.append(i)
              backtrack(i + 1, subset)
              subset.pop()

      backtrack(1, [])

    generate_subsets(number)