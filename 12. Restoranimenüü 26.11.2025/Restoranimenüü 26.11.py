class Menuu:
    def __init__(self, nimi, hind: float):
        self.nimi = nimi
        self.hind = round(hind, 2)
        
    def meetod(self):
        print(f"{self.nimi}, {self.hind}")
        
class Jook(Menuu):
    def __init__(self, nimi, hind: float, suurus):
        super().__init__(nimi, hind)
        self.suurus = suurus
    def kirjeldus(self):
        print(f"Jook: {self.suurus}, {self.nimi}, {self.hind} €")
        
class Toit(Menuu):
    def __init__(self, nimi, hind: float, vürtsikus):
        super().__init__(nimi, hind)
        self.vürtsikus = vürtsikus
        if vürtsikus < 1:
            self.vürtsikus = 1
        elif vürtsikus > 5:
            self.vürtsikus = 5
        else:
            self.vürtsikus = vürtsikus
            
    def kirjeldus(self):
        print(f"Toit: Vürts: {self.vürtsikus}, {self.nimi}, {self.hind}€")
        
Menüü=[
    Jook("Apelsiini mahl", 2.45, "Väike"),    
    Jook("Vedel kartul", 1.25, "Suur"),
    Toit("Sinine kurk", 5.45, 4)
]
        
for item in Menüü:
    item.kirjeldus()