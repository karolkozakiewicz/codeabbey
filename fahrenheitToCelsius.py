input = input().split()
numbers = input[1:]
answer = []
def converting(num):
    answer.append(round((int(number) - 32) * (5 / 9)))
for number in numbers:
    converting(number)
print(*answer)