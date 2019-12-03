import math
def ptheorem(n):
    answer = []
    for i in range(int(n)):
        sides = input().split()
        a, b, c = int(sides[0]), int(sides[1]), int(sides[2])
        hypo = int(math.sqrt(a**2 + b**2))
        if c == hypo:
            answer.append("R")
        else:
            if int(max(a, b, c)) < hypo:
                answer.append("A")
            elif int(max(a, b, c)) > hypo:
                answer.append("O")
    print(*answer)
ptheorem(input())
