class Pangakonto:
    rahasumma1 = 0
    rahasumma2 = 0
    
    def __init__(self, kontoSeis, omanikuNimi):
        self.kontoSeis = kontoSeis
        self.omanikuNimi = omanikuNimi
    
    def rahaLisamine(self):
        if Pangakonto.rahasumma1 <= 0:
            print("Ei ole võimalik raha sisestada.")
        else:
            self.kontoSeis += Pangakonto.rahasumma1
            
    def rahaValjavotmine(self):
        if Pangakonto.rahasumma2 <= 0 or self.kontoSeis == 0:
            print("Ei ole võimalik raha välja võtta.")
        else:
            if self.kontoSeis >= Pangakonto.rahasumma2:
                self.kontoSeis -= Pangakonto.rahasumma2
            else:
                print("Ei ole piisavalt raha.")
                
    def setRahasumma1(self, rahasumma1):
        Pangakonto.rahasumma1 = rahasumma1
        
    def getRahasumma1(self):
        return Pangakonto.rahasumma1
    
    def setRahasumma2(self, rahasumma2):
        Pangakonto.rahasumma2 = rahasumma2
        
    def getRahasumma2(self):
        return Pangakonto.rahasumma2
    
    def andmed(self):
        print("Kontoseis:", self.kontoSeis)
        print("Omaniku nimi:", self.omanikuNimi)
        
konto1 = Pangakonto(100,"Priit")
konto1.setRahasumma1(-5)
konto1.setRahasumma2(-10000)
konto1.rahaLisamine()
konto1.rahaValjavotmine()
konto1.andmed()

konto2 = Pangakonto(200000,"Mandem")
konto2.setRahasumma1(1924)
konto2.setRahasumma2(1555)
konto2.rahaLisamine()
konto2.rahaValjavotmine()
konto2.andmed()