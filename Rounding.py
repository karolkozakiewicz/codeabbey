answer = []
n = int(input("data:\n"))
a = 0
for i in range (n):
    a = input().split()
    b = answer.append(round(int(a[0]) / int(a[1])))
print(*answer)
