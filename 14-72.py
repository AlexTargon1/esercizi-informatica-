# programma che scrive la differenza tra due numeri a e b
# se il loro prodotto è maggiore di 10 oppure la loro somma
# se il loro prodotto è minore di 10
numero1 = int(input("inserire il primo numero = "))
numero2 = int(input("inserire il secondo numero = "))
prodotto = numero1*numero2
if prodotto > 10:
    print(numero1-numero2)
else:
    print(numero1+numero2)
