class Sissekanne:
    
    def __init__(self, tyyp, kuupaev, tundideArv, hinne=""):
        self.tyyp = tyyp
        self.kuupaev = kuupaev
        self.hinne = hinne
        
        if tundideArv >= 1 and tundideArv <= 10:
            self.tundideArv = tundideArv
        else:
            raise ValueError("Tunnid peavad olema vahemikus 1-10")
        if tyyp == "Teooria":
            self.sissekandeVarv = "Valge"
        elif tyyp == "Praktiline":
            self.sissekamdeVarv = "Roheline"
        else:
            self.sissekandeVarv = "Kollane"
        
        
    def muudaHinnet(self, hinne=""):
        self.hinne = hinne
        
    def muudaTyyp(self, tyyp):
        if tyyp == "Teooria":
            self.sissekandeVarv = "Valge"
        elif tyyp == "Praktiline":
            self.sissekandeVarv = "Roheline"
        else:
            self.sissekandeVarv = "Kollane"
            
tunniSissekanne = Sissekanne("Teooria", "12.11.2025", 10, "A")
tunniSissekanne.muudaHinnet("5")
tunniSissekanne.muudaTyyp("Kollane")
print(tunniSissekanne.tyyp)
print(tunniSissekanne.hinne)
print(tunniSissekanne.sissekandeVarv)