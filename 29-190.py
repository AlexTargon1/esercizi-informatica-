# scrivi un programma che legga un reddito
# da tastiera e calcoli l'importo dell'imposta
# sul reddito e la tassazione media

fascia_redditi = {
    15000: 0.23,
    28000: 0.27,
    55000: 0.38,
    75000: 0.41,
    10**12: 0.43,
}
imposta = 0
while True:
    stipendio = int(float(input("A quanto ammonta lo stipendio mensile?\n")))
    if stipendio <= 10**12:
        for i in range (len(fascia_redditi)):
            lista_fascia_redditi = list(fascia_redditi)
            if stipendio > lista_fascia_redditi[i] - lista_fascia_redditi[i-1]:
                if i == 0:
                    imposta += lista_fascia_redditi[i] * fascia_redditi.get(lista_fascia_redditi[i])
                    stipendio -= lista_fascia_redditi[i]
                else:
                    imposta += (lista_fascia_redditi[i] - lista_fascia_redditi[i-1]) * fascia_redditi.get(lista_fascia_redditi[i])
                    stipendio -= lista_fascia_redditi[i] - lista_fascia_redditi[i-1]
            else:
                imposta += stipendio * fascia_redditi.get(lista_fascia_redditi[i])
                stipendio = 0
        print(imposta)
    else:
        print("Impossibile definire un'imposta per questo reddito.")        
    scelta = input("Interrompere il programma? ")
    if scelta == "si":
        break

