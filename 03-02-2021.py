#progamma che fornitogli un dizionario con studenti e voti,
#restituisca un dizionario con gli studenti suddivisi per 
#intervallli di media di voto

studenti = []
voti = []
numero_studente = 0
numero_voto = 1
dic_studente_voti={}

def media_voti():
    while True:
        print("inserire il nome dello studente e poi i voti, scrivere fine per terminare il programma e restituire il dizionario")
        nome_studente = input("nome studente = ")
        if nome_studente != -1:
            studenti.append[nome_studente]
            print("scrivere i voti presi dallo studente", studenti[numero_studente])
            print("se non ha più voti, digitare -1")
            while True:
                print("voto ", numero_voto," = ")
                numero_voto += 1
                voto_studente = int(input(""))
                if voto_studente == -1:
                    dic_studente_voti[studenti[numero_studente]] = voti
                    voti.pop(0:-1)
                    numero_studente += 1
                    break
                else:
                    voti.append[voto_studente]
                    continue
        else:
            print(dic_studente_voti)
            while True:
            (dic_studente_voti[studenti[0]])
            


            

