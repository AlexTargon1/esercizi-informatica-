#partendo da un dizionario con nazioni come chiavi e 
#le capitali come valori,interroga il dizionario
#per visualizzare la capitale della nazione richiesta

nazioni = []
capitali = []
dic = {}
x = 0
y = 0
while True:
    nazione = input("nazione = ")
    nazioni.append(nazione)
    scelta_uno = input("aggiungere nazioni? ")
    if scelta_uno == "si":
        print(nazioni)
    else:
        break
while True:
    print("capitale ",nazioni[x],"= ")
    capitale = input(" ")
    capitali.append(capitale)
    x += 1
    if len(capitali) == len(nazioni):
        break
    else:
        continue
while True:
    dic[nazioni[y]] = capitali[y]
    y += 1
    if y == x:
        break
    else:
        continue
while True:
    nazione_richiesta = input("inserire la nazione di cui si vuole\
 sapere la capitale = ")
    print(dic.get(nazione_richiesta, "nazione non presente nel dizionario"))
    continue
