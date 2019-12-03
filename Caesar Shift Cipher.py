nk = input().split()
n, k = int(nk[0]), int(nk[1])
finalanswer = ''
for i in range(n):
    answer = ''
    text = input().split()
    for word in text:
        
        
        for letter in word:
            letter = letter.upper()
            letter = ord(letter)
            
            if letter != 46:
                letter -= k
                if letter > 90:
                    letter -= 26
                elif letter < 65:
                    letter += 26
             
            answer += str(chr(letter))
        answer += " "
    finalanswer += answer

print(finalanswer)
