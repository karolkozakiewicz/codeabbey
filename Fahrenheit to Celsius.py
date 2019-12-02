def fahrenheitToCelsius():
    answer = []
    x = input().split()
    for i in range(int(x[0])):
        answer.append(round((int(x[i+1])-32)/1.8))
    print(*answer)

fahrenheitToCelsius()
