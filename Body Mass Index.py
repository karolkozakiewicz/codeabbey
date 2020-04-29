"""
weight = kilograms (example: 80)
height = meters (example: 1.73)
"""
def bmi():
    data = input().split()
    weight = int(data[0])
    height = float(data[1])
    bmi = weight / (height**2)
    bmi = float("%.2f" % bmi)

    if bmi < 18.5:
        return "under "
    elif bmi >= 18.5 and bmi < 25.0:
        return "normal "
    elif bmi >= 25.0 and bmi < 30.0:
        return "over "
    elif bmi >= 30.0:
        return "obese "

tries = int(input())
for _ in range(tries):
    print(bmi())