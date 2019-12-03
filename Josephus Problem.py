n = int(input("Ile osob? "))
k = int(input("Co ktora osoba? "))
q = k-1
iloscOsob = [n for n in range(1, n+1)]

while len(iloscOsob) > 1:
    zabity = iloscOsob.pop(q)
    q = (q + (k-1)) % len(iloscOsob)
    print(len(iloscOsob), "[" + str(zabity) + "]")
print(iloscOsob)
