class Prodotto(object):
    prezzo = 0.00
    descrizione = ""
    numero = 0

    def assegna_descrizione(self, descrizione):
        self.descrizione = descrizione
    
    def assegna_prezzo(self, prezzo):
        self.prezzo = prezzo
    
    def n_prodotti(self, numero):
        self.numero = numero

    def visualizza(self):
        print("")
        print("descrizione: ", self.descrizione,)
        print("prezzo: ", self.prezzo," euro")
        print("numero prodotti:", self.numero)

def main():
    prodotto = Prodotto()
    desc = input("descrizione = ")
    prezzo = input("prezzo = ")
    n = input("numero prodotti = ")
    prodotto.assegna_descrizione(desc)
    prodotto.assegna_prezzo(prezzo)
    prodotto.n_prodotti(n)
    prodotto.visualizza()

main()
