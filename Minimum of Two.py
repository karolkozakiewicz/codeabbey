answer = []
n = int(input())
for i in range (n):
    a = input().split()
    answer.append(min(int(a[0]), int(a[1])))
print(*answer)
