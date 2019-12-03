answer = []
for i in range(int(input())): 
    numbers = input().split()
    a, b = int(numbers[0]), int(numbers[1])
    ab = a*b
    while a != b:
        if a > b:
            a = a - b
        elif a < b:
            b = b - a

    gcd = a
    lcm = int(ab / gcd)
    result = "(" + str(gcd) + " " + str(lcm) + ")"
    answer.append(result)
print(*answer)
