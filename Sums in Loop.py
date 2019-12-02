answer = []
for i in range(int(input())):
    a = input().split()
    answer.append(int(a[0]) + int(a[1]))
print(*answer)
