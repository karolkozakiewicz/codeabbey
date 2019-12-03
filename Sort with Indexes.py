answer = []
n = input()
lista = input().split()
nowaLista = [int(i) for i in lista]
nowaLista.sort()
for i in nowaLista:
    j = lista.index(str(i)) + 1
    answer.append(j)

print(*answer)
