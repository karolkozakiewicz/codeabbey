import math
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

tries = int(input())

for x in range(tries):
    numbers = input().split()
    answer = int(numbers[0])/int(numbers[1])
    print(normal_round(answer), '')
