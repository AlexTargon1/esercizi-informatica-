listacifre = []
listacifre1 = []
a = 0
b = 0
c = 0
potenza = 1
cifre = int(input("inserisci la lunghezza del numero binario = "))
while a != (cifre):
    a += 1
    print("inserisci la cifra ",a," = ")
    cifra = int(input())
    listacifre.append(cifra)
    listacifre1.insert(0, cifra)
else:
    listacifre.reverse
    while b != (cifre):
        b += 1
        listacifre[0] *= (potenza)
        potenza *= 2
        c += listacifre[0]
        listacifre.pop(0)
    else:
        print("numero binario = ",listacifre1)
        print("numero decimale = ",c)

        

        


    


