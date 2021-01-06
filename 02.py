figura = input("calcolare l'area di un triangolo, quadrato, rettangolo o cerchio? ")
if figura == "triangolo":
    base = int(input("base = "))
    altezza = int(input("altezza = "))
    area = ((base*altezza)/2)
    print("area del triangolo = ",area)
elif figura == "quadrato":
    lato = int(input("lato = "))
    area = (lato**2)
    print("area del quadrato = ",area)
elif figura == "rettangolo":
    base = int(input("base = "))
    altezza = int(input("altezza = "))
    area = (base*altezza)
    print("area del rettangolo = ")
elif figura == "cerchio":
    raggio = int(input("raggio = "))
    area = ((raggio**2)*3.14)
    print("area del cerchio = ")

