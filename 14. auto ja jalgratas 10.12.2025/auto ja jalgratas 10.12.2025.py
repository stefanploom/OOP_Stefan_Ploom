class Soiduk:
    def __init__(self, mark: str, aasta: int, kiirus):
        self.mark = mark
        self.aasta = aasta
        self.kiirus = kiirus
    
    def soida(self, km, labisoit):
        print("s")
    
class Auto(Soiduk):
    def __init__(self, kütus):
        super().__init__(self, mark, aasta, kiirus)
        self.kütus = kütus
        if kiirus >= 0 or kiirus <= 100:
            self.kiirus = kiirus
    def kiirenda(self):
        if self.kütus >= 1:
            self.kiirus += 10
            self.kütus -= 0.5
            if self.kiirus >= 200:
                self.kiirus = 200
                print("Rohkem kiirendada ei saa")
        else:
            self.kiirus = 0
            print("Kütus sai otsa")
    
    def tankida(self, liitrid: int):
        self.liitrid += self.kütus
        if self.liitrid >= 60:
            print("Kütust ei saa juurde enam lisada")
            self.kütus = 60

class Jalgratas(Soiduk):
    def __init__(self, ratturiEnergia):
        super().__init__(self, mark, aasta, kiirus)
        self.ratturiEnergia = ratturiEnergia
        if ratturiEnergia > 100 or ratturiEnergia < 0:
            self.ratturiEnergia = ratturiEnergia
            
    def kiirenda(self):
        if self.ratturiEnergia >= 10:
            self.kiirus += 5
            self.ratturiEnergia -= 10
            if self.kiirus >= 200:
                self.kiirus = 200
                print("Rohkem kiirendada ei saa")
        else:
            self.kiirus = 0
            print("Energia sai otsa")
    
    def puhka(self, minutid):
        self.ratturiEnergia += minutid / 2
        if ratturiEnergia > 100:
            self.ratturiEnergia = 100
            print("Enam puhata ei saa, energia on täis")
        