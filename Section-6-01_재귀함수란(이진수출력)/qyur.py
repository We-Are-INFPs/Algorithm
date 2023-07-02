import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    number = int(input())

    def getBinary(number):
      if number == 0:
        return '0'
      if number == 1:
        return '1'

      if (number % 2 == 0):
        return getBinary(number // 2) + '0'
      else:
        return getBinary(number // 2) + '1'

    print(getBinary(number))