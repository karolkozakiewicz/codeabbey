n = int(input())
answer = []
a, b, c = (18.5), (25), (30)
for i in range(n):
    x = input().split()
    bmi = float(x[0]) / (float(x[1])*float(x[1]))
    if bmi < float(a):
        answer.append("under")
    elif bmi >= float(a) and bmi < float(b):
        answer.append("normal")
    elif bmi >= float(b) and bmi < float(c):
        answer.append("over")
    elif bmi > float(c):
        answer.append("obese")
print(*answer)
