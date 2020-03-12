tries = int(input())

def calculate(numbers):
    first = int(numbers[0]) * int(numbers[1]) + int(numbers[2])
    first = str(first)
    x=0
    for number in first:
        x += int(number)
    return x

for x in range(tries):
    numbers = input().split()
    print(calculate(numbers), '')