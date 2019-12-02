answer = []
n = int(input())
for n in range(n):
    x = input().split()
    a, b, c = int(x[0]), int(x[1]), int(x[2]) 
    #suma dwóch dowolnych boków większa lub równa pozostałemu bokowi
    if a + b >= c and a + c >= b and b + c >= a:
        answer.append(1)
    else:
        answer.append(0)
print(*answer)
