alunni = 0
lanci = 0
a = 0
listaalunni = []
listalanci = [0]
while True:
    alunni += 1
    lanci += 1
    print("nome alunno ",alunni," = ")
    alunno = input()
    print("lancio in metri alunno ",lanci," = ")
    lancio = int(input())
    if lancio > (listalanci[0]):
        listalanci.append(lancio)
        listalanci.reverse()
        listaalunni.append(alunno)
        listaalunni.reverse()
    else:
        listalanci.append(lancio)
        listaalunni.append(alunno)
    scelta = input("vuoi aggiungere altri alunni? ")
    if scelta == ("si"):
        breakpoint
    else:
        print("vincitore = ",listaalunni[0])
        print("lancio = ",listalanci[0], " metri")
        break

        

