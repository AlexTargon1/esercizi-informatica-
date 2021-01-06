a = 0
b = 0
numero = int(input("numero di città nella lista = "))
escursione = int(input("valore dell'escursione termica da controllare = "))
while a != (numero):
    a += 1
    print("nome città numero ",a," = ")
    nomecittà = input()
    tempmin = int(input("temperatura minima del giorno = "))
    tempmax = int(input("temperatura massima del giorno = "))
    escursionecittà = (tempmax-tempmin)
    if escursionecittà > (escursione):
        b += 1
    else:
        b += 0
    breakpoint
else:
    print("numero città registrate dal contatore = ",b)
    







