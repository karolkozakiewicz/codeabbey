answer = []
sum = []
#print("input data:")
n = int(input())
for i in range (n):
    answerM = 0
    x = input().split()
    a, b, c = int(x[0]), int(x[1]), int(x[2])
    d = a*b+c
      
    while d >= 10:
        sum.append(int(d%10))
        d = int((d-(int(d%10)))/10)
        
        if d < 10:
            sum.append(d)
    
    for i in(sum):
        answerM = answerM + i
    
    answer.append(answerM)
    sum.clear()

print(*answer)
