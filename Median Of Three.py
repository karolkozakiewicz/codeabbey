tries = int(input())

for x in range(tries):
    numbers = input().split()
    numbers = list(map(int, numbers))
    numbers.sort()
    print(numbers[1],'')