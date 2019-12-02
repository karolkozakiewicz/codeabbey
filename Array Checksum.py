result = 0
n = int(input())
x = input().split()
for i in x:
    item = ((result + int(i)) * 113) % 10000007
    result = item
print(result)
