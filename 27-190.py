# organizza con un dizionario la rubrica con i nomi delle persone 
# e i rispettivi numeri telefonici, fornitogli poi il nome della
# persona, il programma visualizza il suo numero di telefono oppure 
# un messaggio nel caso in cui la persona non sia nella rubrica 

rubrica_chiave_numero = {}
rubrica_chiave_nomi = {}
n_numeri = int(input("quanti numeri vorresti inserire nel dizionario? "))
while n_numeri != 0:
    nome = input("nome = ")
    numero = int(input("numero di telefono = "))
    rubrica_chiave_numero[numero] = nome
    n_numeri -= 1
for i in rubrica_chiave_numero:
    rubrica_chiave_nomi[rubrica_chiave_numero[i]] = i
while True:
    print("nome della persona di cui si vuole sapere il numero = ")
    nome_da_chiedere = input()
    if nome_da_chiedere in rubrica_chiave_nomi:
        print("numero di telefono = ", rubrica_chiave_nomi[nome_da_chiedere])
    else:
        print("questo nome non è nella rubrica")
    scelta = input("vuoi sapere il numero di qualche altra persona? ")
    if scelta == "si":
        continue
    else:
        print("grazie per aver utilizzato il programma")
        break
        

