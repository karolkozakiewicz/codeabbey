tries = int(input())
answer = []
for x in range(tries):
    values = input().split()
    answer.append(int(values[0])+int(values[1]))

print(*answer)