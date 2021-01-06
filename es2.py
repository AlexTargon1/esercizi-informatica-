nome1 = input("nome del primo candidato = ")
nome2 = input("nome del secondo candidato = ")
punteggio1 = int(input("punteggio del primo candidato = "))
punteggio2 = int(input("punteggio del secondo candidato = "))
listacandidati = [nome1, nome2]
listacandidati.sort()
print(listacandidati)
if punteggio1<punteggio2:
    print([nome1, nome2])
else:
    print([nome2, nome1])