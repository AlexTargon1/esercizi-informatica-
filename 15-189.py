#programma che dato un elenco di nazioni contenuto in una lista e uno
#delle rispettive capitali in una seconda lista, visualizzi la capitale
#di una nazione della quale viene fornito da tastiera il nome, segnalando
#con un messaggio di errore il caso in cui la nazione richiesta non sia
#compresa nell'elenco

dic = {}
while True:
    nazione = input("nazione = ")
    capitale = input("capitale = ")
    dic[nazione] = capitale
    scelta = input("vuoi aggiungere nazioni? ")
    if scelta == "si":
        print(dic)
    else:
        print(dic)
    while True:
        nazione_richiesta = input("di quale nazione vuoi sapere la capitale? ")
        print(dic.get(nazione_richiesta, "errore: nazione non compresa nella lista"))
        continue

    

