answer = []
swaps = 0
result = 0
n = input().split()
m = n[:len(n)-1]
for i in range(len(m)):
    if i+2 <= len(m):
        if m[i] < m[i+1]:
            pass
        elif m[i] > m[i+1]:
            t = m[i]
            m[i] = m[i+1]
            m[i+1] = t
            swaps += 1
    item = ((result + int(m[i])) * 113) % 10000007
    result = item

answer.append(swaps)
answer.append(result)
    
print(*answer)
