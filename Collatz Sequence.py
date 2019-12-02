def collatz(n):
    answer = []
    x = input().split()
    for i in range(int(n)):
        counter = 0
        while int(x[i]) != 1:
            if int(x[i])%2 == 0:
                x[i] = int(x[i])/2
                counter += 1
            else:
                x[i] = int(x[i])*3 + 1
                counter += 1
        answer.append(counter)
    print(*answer)

collatz(input())
