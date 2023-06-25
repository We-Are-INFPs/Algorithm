import sys
for tc in range(1, 6):
    sys.stdin = open(f'in{tc}.txt', 'rt')
    n, m = map(int, input().split())
    people = list(map(int, input().split()))
    risk = sorted(people, reverse=True)
    pointer = m
    count = 0
    while 1:
        if people[0] == risk[0]:
            people.pop(0)
            risk.pop(0)
            count += 1
            if pointer == 0:
                break
            else:
                pointer -= 1
        else:
            popped = people.pop(0)
            people.append(popped)
            if pointer == 0:
                pointer = len(people) - 1
            else:
                pointer -= 1

    print(count)
