answer = []

def RockPaperScissors(a,b):
    global aWins, bWins, draw
    a, b = a.upper(), b.upper()
    if a == "S": #scissors
        if b == "R":
            bWins += 1
        elif b == "S":
            draw += 1
        elif b == "P":
            aWins += 1
    if a == "R": #rock
        if b == "S":
            aWins
            aWins += 1
        if b == "R":
            draw += 1
        if b == "P":
            bWins += 1
    if a == "P": #paper
        if b == "S":
            bWins += 1
        if b == "P":
            draw += 1
        if b == "R":
            aWins += 1

for i in range(int(input())):
    aWins, bWins, draw = 0, 0, 0
    x = input().split()
    for pair in x:
        a, b = pair[0], pair[1]
        RockPaperScissors(a, b)
    #print("a: ",aWins, "b: ",bWins, "draw: ",draw)
    if aWins > bWins:
        answer.append(1)
    elif aWins < bWins:
        answer.append(2)

print(*answer)
