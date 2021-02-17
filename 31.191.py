# dopo aver acquisito in un array il fatturato nelle quattro 
# zone, calcola: il totale del fatturato e i valori in
# percentuale delle vendite nelle quattro zone rispetto
# al totale

while True:
    fatturato = 0
    dic = {}
    f_nord = int(input("fatturato della zona Nord = "))
    f_centro = int(input("fatturato della zona Centro = "))
    f_sud = int(input("fatturato della zona Sud = "))
    f_isole = int(input("fatturato della zona delle isole = "))
    dic["Nord"] = f_nord
    dic["Centro"] = f_centro
    dic["Sud"] = f_sud
    dic["Isole"] = f_isole
    lista_dic = list(dic)
    for n in range(len(lista_dic)):
        fatturato += dic.get(lista_dic[n])
    percentuale_nord = (f_nord/fatturato)*100
    percentuale_centro= (f_centro/fatturato)*100
    percentuale_sud = (f_sud/fatturato)*100
    percentuale_isole = (f_isole/fatturato)*100
    print("fatturato = ", fatturato, " euro")
    print("percentuale fatturato Nord = ", percentuale_nord, "%")
    print("percentuale fatturato Centro = ", percentuale_centro, "%")
    print("percentuale fatturato Sud = ", percentuale_sud, "%")
    print("percentuale fatturato delle isole = ", percentuale_isole, "%")
    scelta = input("continuare? ")
    if scelta != "si":
        break

    
