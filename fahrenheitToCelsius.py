input = input().split()
tries = input[0]
numbers = input[1:]
answer = []
for number in numbers:
    answer.append(round((int(number) - 32)*(5/9)))
print(*answer)