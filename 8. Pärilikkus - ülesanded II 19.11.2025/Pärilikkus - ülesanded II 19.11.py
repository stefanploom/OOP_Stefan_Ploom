class Loomad:
    def __init__(self, kasOnJalad: bool, korgus: int, toitumine: str, vanus: int):
        self.kasOnJalad = kasOnJalad
        self.korgus = korgus
        self.toitumine = toitumine
        self.vanus = vanus

        if toitumine not in ["Taime", "Liha", "Segu"]:
            raise ValueError("Toitumine peab olema Taime, Liha või Segu")

    def kasva(self, kasv):
        self.korgus += kasv

    def vanane(self, vana):
        self.vanus += vana

class Imetajad(Loomad):
    def __init__(self, kasOnJalad: bool, korgus: int, toitumine: str, vanus: int, sugu: str):
        super().__init__(kasOnJalad, korgus, toitumine, vanus)
        self.sugu = sugu

        if sugu not in ["M", "N"]:
            raise ValueError("Sugu peab olema M või N")

    def sure(self):
        if self.vanus > 211:
            print("Imetaja on surnud, vanemaid imetajaid ei ole olnud")

class Inimesed(Imetajad):
    def __init__(self, kasOnJalad: bool, korgus: int, toitumine: str, vanus: int, sugu: str, nimi: str, kodakondsus: str):
        super().__init__(kasOnJalad, korgus, toitumine, vanus, sugu)
        self.nimi = nimi
        self.kodakondsus = kodakondsus

    def sure(self):
        if self.vanus > 121:
            print(self.nimi + " on surnud, vanimat inimest ei ole olnud")

    def valjastaAndmed(self):
            print("Tere", self.nimi, ", sa oled pärit riigist", self.kodakondsus, ". Sa oled", self.vanus, "aastat vanan ning oled", self.korgus, "cm kõrge. sa oled " + self.sugu + " soost ja sa oled", self.toitumine, "toitlane.")
        
Iku=Inimesed(True, 120, "Segu", 102, "N", "Priit", "Rootsi")
Iku.valjastaAndmed()

