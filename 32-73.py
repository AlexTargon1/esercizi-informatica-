a = int(input("valore di a = "))
b = int(input("valore di b = "))
if a == 0:
    if b == 0:
        print("equazione indeterminata")
    else:
        print("equazione impossibile")
else:
    if b == 0:
        print("x = 0")
    else:
        x = -(b/a)
        print("x = ",x)
