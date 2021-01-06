listabinario = []
numero = int(input("numero decimale da transformare in binario = "))
numero2 = numero
while numero != (0):
    numero1 = numero % (2)
    listabinario.insert(0, numero1)
    numero //= (2)
else:
    print("numero decimale = ",numero2)
    print("numero binario = ",listabinario)
