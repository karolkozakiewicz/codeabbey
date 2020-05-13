def josephus(n, k):
    list = [_ for _ in range(1,n+1)]
    k2 = k - 1
    k = k2
    while len(list) > 1:
        list.pop(k)
        k = (k + k2) % len(list)
    print(*list, " ")

inp = input().split()
n = int(inp[0])
k = int(inp[1])

josephus(n, k)

