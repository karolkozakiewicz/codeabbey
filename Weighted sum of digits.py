answer = []
n = int(input())
x = input().split()
for number in range(n):
    t = 1
    #print("number", number)
    sum = 0 #weighted sum of digits in the case
    for digit in x[number]:
        #print("test:", )
        sum += int(digit)*t
        t += 1
     
    answer.append(sum)
print(*answer)
