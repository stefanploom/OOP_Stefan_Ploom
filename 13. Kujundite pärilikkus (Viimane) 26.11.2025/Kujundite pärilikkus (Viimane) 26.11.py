class kujund:
    def pindala(self):
        return 0

class Ruut(kujund):
    def __init__(self, külg):
        self.külg = külg
    def pindala(self):
        pindala = self.külg * self.külg
        return pindala
    
class Ring(kujund):
    def __init__(self, raadius):
        self.raadius = raadius
    def pindala(self):
        pindala = 3.14 * self.raadius * self.raadius
        return round(pindala, 2)
        
o1 = Ruut(2)
o2 = Ring(4)
o3 = Ruut(200)
o4 = Ring(12)

print("o1 pindala:", o1.pindala())
print("o2 pindala:", o2.pindala())
print("o3 pindala:", o3.pindala())
print("o4 pindala:", o4.pindala())
        