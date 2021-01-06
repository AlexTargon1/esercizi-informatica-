# programma che verifica se il numero
# inserito è pari o dispari
numero = int(input("numero da verificare = "))
resto = numero%2
if resto == 1:
    print("il numero è dispari")
else:
    print("il numero è pari")