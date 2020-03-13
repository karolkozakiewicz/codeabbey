tries = int(input())
answer = []
for x in range(tries):
    a,b,n = input().split()
    odp = 0
    for i in range(int(n)):
        odp += (int(a) + (int(b)*i))
    answer.append(odp)

print(*answer)