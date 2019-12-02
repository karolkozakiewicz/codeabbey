answer = []
for i in range(int(input())):
    y = []
    x = input().split()
    for i in x:
        y.append(int(i))
    answer.append(sorted(y)[1])
print(*answer)
