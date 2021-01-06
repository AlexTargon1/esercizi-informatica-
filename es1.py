nome1 = input("nome del primo candidato = ")
nome2 = input("nome del secondo candidato = ")
nome3 = int(input("punteggio del primo candidato = "))
nome4 = int(input("punteggio del secondo candidato = "))
nome5 = (nome3+nome4)
nome3p = ((nome3/nome5)*100)
nome4p = ((nome4/nome5)*100)
print("la percentuale dei voti del primo candidato = ",nome3p)
print("la percentuale dei voti del secondo candidato = ",nome4p)
if (nome3>nome4):
    print("il vincitore é = ",nome1)
elif (nome3<nome4):
    print("il vincitore é = ",nome2)
else:
    print("é pareggio")
