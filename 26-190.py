# con riferimento al dizionario dell'esercizio 25 pagg. 190,
# elenca i numeri di matricola degli studenti che hanno 
# ottenuto una votazione superiore alla media

dic_chiave_nomi = {}
dic_chiave_voti = {}
studenti = 3
somma_voti = 0
lista_voti = []
lista_migliori = []
while studenti != 0:
    nome_studente = input("nome studente = ")
    voto_studente = int(input("voto studente = "))
    dic_chiave_nomi[nome_studente] = voto_studente
    somma_voti += voto_studente
    lista_voti.append(voto_studente)
    studenti -= 1
media_voti = somma_voti/3
studenti = 0
for i in dic_chiave_nomi:
    dic_chiave_voti[dic_chiave_nomi[i]] = i
while True:
    if lista_voti[studenti] >= media_voti:
        lista_migliori.append(dic_chiave_voti[lista_voti[studenti]])
        studenti += 1
        if studenti == 30:
            break
        else:
            continue
    else:
        studenti += 1
        if studenti == 30:
            break
        else:
            continue
print("gli studenti migliori sono = ", lista_migliori)

        


    


