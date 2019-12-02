answer = []
n = int(input())
for i in range(n):
    average = []
    x = input().split()
    
    for number in range(len(x)-1):
        average.append(int(x[number]))
    
    x = 0
    
    for number in average:
        x += number
        
    x = round(x/len(average))
    answer.append(x)
print(*answer)
