"""
wsd(1776) = 1 * 1 + 7 * 2 + 7 * 3 + 6 * 4 = 60
"""

tries = int(input())
numbers = input().split()

def wsd(number):
    number = str(number)
    answer = []
    for i in range(len(str(number))):
        answer.append( (i+1) * int(number[i])  )
    answer = sum(answer)
    print(answer)

for x in numbers:
    wsd(x)
    print(" ")