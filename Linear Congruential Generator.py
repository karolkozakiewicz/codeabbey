answer = []
for i in range(int(input())):
    counter = 0
    case = input().split()

    a = int(case[0]) #mnożnik
    c = int(case[1]) #składnik
    m = int(case[2]) #modulo
    x0 = int(case[3]) #pierwsza liczba w sekwencji
    n = int(case[4]) #którą liczbę policzyć

    while counter != n:
        x0 = (a * x0 + c) % m
        counter += 1
    answer.append(x0)

print(*answer)
