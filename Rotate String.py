def rotateString(n):
    answer = []
    for i in range(n):
        ms = input().split()
        m, s = int(ms[0]), ms[1]
        answer.append((s[m:]+s[:m]))

    print(*answer)
rotateString(int(input()))
