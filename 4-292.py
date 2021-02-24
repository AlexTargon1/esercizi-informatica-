class Atleta(object):
    def __init__(self, nome, altezza, eta, visita_medica = False):
        self.nome = nome
        self.altezza = altezza
        self.eta = eta
        self.visita_medica = visita_medica

    def squadra(self):
        squadra = input("squadra in cui gioca l'atleta = ")
        self.squadra = squadra
        return self.squadra

    def visita(self):
        self.visita_medica = True

    def visualizza_dati(self):
        print("nome = ", self.nome)
        print("altezza = ", self.altezza)
        print("età = ", self.eta)
        print("squadra = ", self.squadra)
        print("visita medica fatta")

atleta = Atleta("Alessio", 1.78, 19)
atleta.squadra()
atleta.visita()
atleta.visualizza_dati()

