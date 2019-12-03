def neumannsRandomGenerator(n):
    answer = []
    x = input().split()
    for i in range(int(n)):
        array = []
        while x[i] not in array:
            array.append(int(x[i]))
            x[i] = int(x[i])**2
            x[i] = str(x[i])
            while len(str(x[i])) < 8:
                x[i] = "0" + x[i]
            x[i] = (int(x[i])/100)%10000
        answer.append(len(array))
    print(*answer)

neumannsRandomGenerator(input())
    
