answer = []
for i in range(int(input())):
    a = input().split()
    answer.append(min(int(a[0]), int(a[1]), int(a[2])))
print(*answer)
