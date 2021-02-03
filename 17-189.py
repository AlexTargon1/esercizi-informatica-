#programma che dato un dizionario di nazioni come chiave
#con le proprie capitali come valore, inverte la chiave 
# e il valore per poi trovare la nazione conoscendo 
#il nome della capitale

dic_nazioni = {}
print("inserire le nazioni con le rispettive capitali,\
    per poi interrogare il dizionario per trovare le\
    nazioni conoscendone la capitale")
while True:
    nazione = input("nazione = ")
    capitale = input("capitale = ")
    dic_nazioni[nazione] = capitale
    scelta = input("aggiungere altre nazioni? ")
    if scelta == "si":
        continue
    else:
        break
dic_capitali = {}
for nazione in dic_nazioni:
    dic_capitali[dic_nazioni[nazione]] = nazione
print("")
print("se non si vuole più interrogare il dizionario,\
    digitare 'fine'")
print("")
while True:
    capitale = input("capitale = ")
    if capitale == "fine":
        print("grazie per aver utilizzato il programma")
        break
    elif capitale in dic_capitali:
        print(dic_capitali[capitale])
        continue
    else:
        print("non sappiamo di che nazione sia questa capitale, riprova")
        continue
    
    
    