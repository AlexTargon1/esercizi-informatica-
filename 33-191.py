#programma che consente di registrare nomi di pazienti che man mano
#arrivano, visualizandone poi il primo della coda in attesa

lista_pazienti = []
numero_paziente = 1
print("registrare i nomi dei pazienti in coda")
while True:
    print("nome paziente ", numero_paziente," = ")
    paziente = input()
    lista_pazienti.append(paziente)
    numero_paziente += 1
    scelta_uno = input("ci sono altri pazienti in fila? ")
    if scelta_uno == "si":
        continue 
    else:
        break
while True:
    if len(lista_pazienti) == 0:
        print("per oggi, il nostro lavoro qui é finito")
        break
    else:
        print("esame del paziente", lista_pazienti[0], " fatto")
        lista_pazienti.pop(0)
        scelta_due = input("sono arrivati altri pazienti? ")
        if scelta_due == "si":
            attesa_pazienti = int(input("quanti pazienti sono arrivati? "))
            while True:
                print("nome paziente ", numero_paziente," = ")
                paziente = input()
                lista_pazienti.append(paziente)
                numero_paziente += 1
                attesa_pazienti -= 1
                if attesa_pazienti == 0:
                    break
                else:
                    continue
        else:
            continue
                


    


