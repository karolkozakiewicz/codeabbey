answer = []
mn = input().split()
m, n = int(mn[0]), int(mn[1])
lista = input().split()
for i in range(n):
    answer.append(lista.count(str(i+1)))
print(*answer)
