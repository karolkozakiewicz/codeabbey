def palindrom(n):
    answer = []
    for i in range(n):
        sentence = input()
        newSentenceA = '' #sentence without special characters
        newSentenceB = '' #reversed A
        for letter in sentence:
            letter = ord(letter.lower())
            if letter >= 97 and letter <= 122:
                newSentenceA += chr(letter)
        
        for letter in newSentenceA:
            newSentenceB = letter + newSentenceB
        
        if newSentenceA == newSentenceB:
            answer.append("Y")
        else:
            answer.append("N")

    print(*answer)

palindrom(int(input()))
