answer = [] #pusta lista do której dodaję wartości
b = 0 #wartość obecnego minimum
c = 0 #maximum
x = 300 #ilość powtórzeń pętli
a = input("data:\n").split() #rozdzielenie danych po spacji - do listy
for i in range (x):
    if int(a[0+i]) < int(b): #porównywanie kolejnych indexów do b
       b = a[0+i]
       
    elif int(a[0+i]) > int(c):
        c = a[0+i]
        
print("answer:\n")
print(c, b)
