# i voti di una classe di 30 studenti, vengono inseriti come valori in un 
# dizionario con il rispettivo nome dello studente, elencando in ordine 
# crescente di voto e successivamente visualizzando quanli valori diversi
# tra loro sono stati assegnati, riducendo a uno i voti uguali  

dic = {}
studenti = 30
voti_totali = []
while studenti != 0:
    nome_studente = input("nome studente = ")
    voto_studente = int(input("voto studente = "))
    dic[nome_studente] = voto_studente
    studenti -= 1
voti_ordinati = sorted(dic.values())
print(voti_ordinati)
while True:
    if len(voti_ordinati) != 0:
        a = voti_ordinati[0]
        voti_totali.append(a)
        while a in voti_ordinati:
            voti_ordinati.remove(a)
        else:
            continue
    else:
        break
print(voti_totali)





    
