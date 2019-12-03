def calc(n):
    answer = []
   
    for i in range(int(n)):
        years = 0
        srp = input().split()
        s, r, p = float(srp[0]), float(srp[1]), float(srp[2])/100

        while int(s) < int(r):
            s = s + s*p
            s = int(s * 10 ** 2) / 10 ** 2
            years += 1
        answer.append(years)
    print(*answer)
calc(input())
