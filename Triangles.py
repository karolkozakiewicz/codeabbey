tries = int(input())
for x in range(tries):

    numbers = input().split()
    numbers = list(map(int, numbers))
    numbers.sort()

    if numbers[0] + numbers[1] <= numbers[2]:
        print('0 ')
    else:
        print('1 ')