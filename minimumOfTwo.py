tries = int(input())
answer = []
for x in range(tries):
    values = input().split()
    if int(values[0]) > int(values[1]):
        answer.append(int(values[1]))
    else:
        answer.append(int(values[0]))

print(*answer)