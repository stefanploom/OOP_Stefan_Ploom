class Seade:
    km_protsent = 22

    def __init__(self, tootekood, nimetus, hind):
        self.tootekood = tootekood
        self.nimetus = nimetus
        self.hind = hind

    def get_tootekood(self):
        return self.tootekood
    def get_nimetus(self):
        return self.nimetus
    def get_hind(self):
        return self.hind
    def set_tootekood(self, tootekood):
        self.tootekood = tootekood
    def set_nimetus(self, nimetus):
        self.nimetus = nimetus
    def set_hind(self, hind):
        self.hind = hind

    def kmhind(self):
        return self.hind * (1 + Seade.km_protsent / 100)

    def tekstiks(self):
        print("Tootekood:", self.tootekood)
        print("Nimetus:", self.nimetus)
        print("Hind:", self.hind)
        
seade1 = Seade(10131, "Vigur", 5127.24)
seade2 = Seade(13573, "Puulusikas", 4550)
print(seade1.tekstiks())
print(seade2.tekstiks())
print("Käibemaksuga hind (seade1):", seade1.kmhind())
print("Käibemaksuga hind (seade2):", seade2.kmhind())
