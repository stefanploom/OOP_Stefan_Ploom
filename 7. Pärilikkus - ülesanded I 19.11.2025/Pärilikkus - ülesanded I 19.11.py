class Soiduk:
    def __init__(self, maxKiirus, nimi, istekohtadeArv):
        self.maxKiirus = maxKiirus
        self.nimi = nimi
        self.istekohtadeArv = istekohtadeArv

class Buss(Soiduk):
    def __init__(self, maxKiirus, nimi, istekohtadeArv, piletiHind):
        super().__init__(maxKiirus, nimi, istekohtadeArv)
        self.piletiHind = piletiHind
        self.soitjateArv = 12
        
    def ostaPilet(self, arv):
        self.arv = arv
        self.soitjateArv += arv
        print(f"Osteti {arv} piletit. Sõitjaid on nüüd {self.soitjateArv}")

Buss=Buss(100, "priit", 100, 12)
print("Sõiduki nimi:" + Buss.nimi)
print("Sõiduki maksimaalne kiirus:" + str(Buss.maxKiirus))
print("Sõiduki istekohtade arv:" + str(Buss.istekohtadeArv))
print("Sõiduki piletihind:" + str(Buss.piletiHind) + "€")
Buss.ostaPilet(2)