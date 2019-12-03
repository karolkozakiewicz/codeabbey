def bullsAndCows(x):
    answer, secretValue = [], []
    a = str(x[0])
    n = int(x[1])
    b = input().split()
    [secretValue.append(letter) for letter in a]
    
    for i in range(n):
        guess = []
        counter1, counter2 = 0, 0
        [guess.append(letter) for letter in str(b[i])]
        for i in range(len(guess)):
            if guess[i] == secretValue[i]:
                counter1 += 1
            elif guess[i] != secretValue and guess[i] in secretValue:
                counter2 += 1
        answer.append(str(counter1) + "-" + str(counter2))
    print(*answer)

bullsAndCows(input().split())
