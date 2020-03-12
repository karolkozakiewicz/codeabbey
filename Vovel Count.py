tries = int(input())

def vovel_counting(sentence):
    counter = 0
    vovels = ['a', 'i', 'u', 'e', 'o', 'y']
    for vovel in sentence:
        if vovel in vovels:
            counter +=1
    return counter

for x in range(tries):
    sentence = input()
    print(vovel_counting(sentence), '')
