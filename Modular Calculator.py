sum = int(input())
a = ''
while "%" not in a:
    a = input().split()
    if "+" in a:
        sum += int(a[1])
    elif "*" in a:
        sum *= int(a[1])
    
else:
    answer = sum % int(a[1])

print(answer)
