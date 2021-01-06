print ("ciao, mi chiamo Robert e sarò la tua nuova giuda in questo fantastico viaggio")
nome = input("come ti chiami? ")
print("gran bel nome!!")
print("come prima cosa, voglio regalarti un cavallo")
colorecavallo = input("di che colore lo vorresti? ")
listacolorecavallo = ["bianco", "nero", "marrone"]
if colorecavallo in listacolorecavallo:
  print("bellissimo colore")  
else: 
  print("colore insolito per un cavallo")
  colorecavallo1 = input("scegli un colore tra bianco, nero o marrone: ")
  if colorecavallo1 in listacolorecavallo:
    print("bellissimo colore")
  else:
    print("forse non parliamo la stessa lingua, quindi te lo darò bianco")
nomecavallo = input("come lo vuoi chiamare? ")
print("perfetto")
fazioni = ["gnomi", "elfi", "stregoni", "umani"]
fazione = input("in questo mondo esistono 4 fazioni; gnomi, elfi, stregoni e umani, tu a quale fazione appartieni? ")
if fazione in fazioni[0]:
  print("gli gnomi sono sempre stati grandi combattenti, però non vedo dove sia la tua ascia!!")
  print("vabbé, te ne procuro io una, ma la prossima volta cerca di avercela sempre con te")
elif fazione in fazioni[1]:
    print("non vedo le tue orecchie da elfo, sicuro di essere un elfo? hahaha")
    print("vedo che ti manca l'arco, tranquillo, te lo procuro io")
elif fazione in fazioni[2]:
      print("guarda che coincidenza, anche io sono uno stregone hahaha")
      print("presumo che il tuo bastone magico sia stato smarrito dato che non lo vedo con te")
      bastonemagico = input("che potere vuoi che abbia il tuo bastone magico? ci sono infinit poteri, scegline uno: ")
      print("che potere magnifico per uno stregone!!")
elif fazione in fazioni[3]:
        print("umani, creature senza un'effettivo potere, penso che dovrò proteggerti io durante tutta l'avventura")
        print("tieni questa spada e fanne buon uso")
else:
          print("noto che sei un forestiero, tieni questa spada")
          print("la spada é l'arma più facile da utilizzare, non credo tu avrai difficoltà ad usarla")
print("finalmente, che l'avventura abbia inizio!!")
print("il tuo obbiettivo é quello di cacciare via i goblin che si sono insediati nella città che si trova a Est")
via = input("per andare in città, vuoi passare per il sentiero in mezzo al bosco? ")
if via is "si":
  print("perfetto, ma ti assicuro fin da subito che questa via nasconde tante insidie!!")
  oggetto = input("scegli un oggetto da portare con te tra questi: torcia, bussola o cannochiale ")
  if oggetto is "torcia":
    print("davvero molto utile, ti aiuterà per illuminarti il cammino")
    print("oh no, hai avvistato un gruppo di goblin vicino a te!!")
    situazione1 = input("vuoi utilizzare la torcia? ")
    if situazione1 is "si":
      print("hai allarmato i goblin vicino a te!!")
      situazione1A = input("vuoi scappare o affrontarli? ")
      if situazione1A is "scappare":
        print("bravo, sei riuscito a scappare, la prossima volta non rischiare più")
      else:
        print("oh no, i goblin sono troppi, ti hanno ucciso")
        breakpoint
    else:
      print("sei riuscito a nasconderti nel buio e i goblin se ne sono andati")  
      print("adesso riprendi a camminare per il sentiero")
  elif oggetto is "bussola":
    print("ti sarà molto utile per orientarti")
    print("sei arrivato ad un bivvio")
    situazione2 = input("vuoi utilizzare la bussola? ")
    if situazione2 is "si":
      print("la bussola indica che il nord è esattamente davanti a te")
      situazione2A = input("vuoi andare nella via di sinistra o di destra? ")
      if situazione2A is "sinistra":
        print("durante il percorso, ti sei perso e non riesci più a ritrovare la giusta via")
        print("mi dispiace, ma credo che la tua avventura possa finire qui")
        breakpoint
  elif oggetto is "cannocchiale":
    print("ti servirà per scrutare da lontano i pericoli che ti aspetanno")
    situazione3 = input("vuoi utilizzare il cannocchiale per vedere se ci sono pericoli attorno? ")
    if situazione3 is "si":
      print("hai avvistato proprio davanti a te un gruppo di goblin")
      situazione3A = input("vuoi girare nel sentiero alla tua destra? ")
      if situazione3A is "si":
        print("bravo, sei riuscito a seminare i goblin")
        print("puoi continuare per il sentiero")
      else:
        print("i goblin ti hanno visto, mi sa proprio che la tua avventura finiasce qui")
        breakpoint
    else:
      print("c'è un sentiero alla tua destra")
      situazione4 = input("vuoi girare nel sentiero a destra? ")
      if situazione4 is "si":
        print("bravo, sei riuscito a seminare i goblin")
        print("continua per il sentiero")
else:
  print("allora dobbiamo per forza prendere la strada che porta verso il fiume")  
  print("siamo arrivati al fiume e c'è una barca e un ponte")
  situazione5 = input("vuoi attraversare il fiume con la barca? ")
  if situazione5 is "si":
    print("oh no, la barca si é distrutta e sei caduto in acqua")
    print("sei morto affogato, l'avventura non é andata proprio a buon fine")
    breakpoint
  else:
    print("sei passato per il ponte ed é andato tutto bene")
    print("continua a camminare")
print("sei arrivato in città")
situazione6 = input("vuoi provare a combattere i goblin? ")
if situazione6 is "si":
  print("i goblin sono fin troppi!!")
  situazione7 = input("vuoi provare a scappare dalla città? ")
  if situazione7 is "si":
    print("sei scappato dalla città e ti sei salvato la pelle, ma hai fallito la tua missione")
    breakpoint
  else:
    print("sei morto combattendo, ma hai fallito lo stesso e la città rimarra sotto assedio ancora per molto..")
    breakpoint
else:
  print("hai appena notato che tutti i goblin sono dentro a quella casa")
  situazione8 = input("vicino a loro ci sono delle botti di polvere da sparo, le vuoi far esplodere? ")
  if situazione8 is "si":
    print("bravissimo, complimenti davvero, sei riuscito a salvare la città")
  else:
    print("i goblin ti hanno visto e ti hanno circondato")
    print("ti hanno preso come prigioniero e in prigione marcirai, hai fallito")
