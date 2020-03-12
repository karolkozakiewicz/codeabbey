numbers = input().split()
numbers = map(int,numbers)
answer = sorted(numbers)
print(answer[-1], answer[0])