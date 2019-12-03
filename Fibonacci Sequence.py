def fibonacci(n):
    answer = []
    for i in range(int(n)):
        x = int(input())
        fibonacci = [0, 1]
        d = 0
        for i in range(1000):
            fibonacci.append(int(fibonacci[0+i])+int(fibonacci[1+i]))
        while x != fibonacci[d]:
            d += 1
        else:
            answer.append(d)
    print(*answer)

n = input()
fibonacci(n)
