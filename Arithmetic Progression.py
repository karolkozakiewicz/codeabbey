sum = [] #pula wszystkich składników
answer = [] #ostateczna odpowiedź
c = 0 #dodawanie składników
x = int(input())  #ilość przypadków
for i in range (x):
    abn = input().split()
    a, b, n = int(abn[0]), int(abn[1]), int(abn[2]) #first value, step
    
    for i in range (n):
        ans = a + i * b
        sum.append(ans)
       
    for i in (sum):
      i = int(i)
      c = c + i
     
    answer.append(c)
    sum.clear()
    c = 0
   
print(*answer)
