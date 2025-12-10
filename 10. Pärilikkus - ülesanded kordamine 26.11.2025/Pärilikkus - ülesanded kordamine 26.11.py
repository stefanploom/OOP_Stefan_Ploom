class Raamat:
    def __init__(self, pealkiri, autor, zanr, saadavus: bool):
        self.pealkiri = pealkiri
        self.autor = autor
        self.zanr = zanr
        self.saadavus = saadavus

class Raamatukogu(Raamat):
    def __init__(self, pealkiri, autor, zanr, saadavus: bool):
        super().__init__(pealkiri, autor, zanr, saadavus)
    
    def LaenutaRaamat(self):
        if self.saadavus is True:
            self.saadavus is False
            ("Raamat on laenutatud")
        else:
            print("Raamatut ei ole võimalik välja laenata, on juba välja laenatud")
            
    def TagastaRaamat(self):
        if self.saadavus is False:
            self.saadavus is True
            print("Raamat on tagastatud")
        else:
            print("Raamatut ei ole võimalik tagastada, on juba tagastatud.")

    def VäljastaAndmed(self):
        print(f"Raamat nimega {self.pealkiri} kirjutas autor {self.autor}. Raamatu žanr on {self.zanr} ning raamat on hetkel {self.saadavus}")

Laheraamat=Raamatukogu("Raamar", "Priit", "Hea", False)
Laheraamat.VäljastaAndmed()
Laheraamat.LaenutaRaamat()