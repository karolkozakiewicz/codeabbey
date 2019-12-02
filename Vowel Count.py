answer = []
counter = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
n = int(input())
for i in range(n):
    case = input().split()
    
    for word in case:
        
        for letter in word:
           
            if letter in vowels:
                counter += 1
    answer.append(counter)
    counter = 0
print(*answer)
