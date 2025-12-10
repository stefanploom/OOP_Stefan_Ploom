class Loomad:
    def Häälitsus(self):
        print("")
        
class Mesilased(Loomad):
    def Häälitsus(self):
        print("Bzz bzz")
        
class Kalad(Loomad):
    def Häälitsus(self):
        print("Mull mull")
        
class Sead(Loomad):
    def Häälitsus(self):
        print("Röhh röhh")
        
class Öökullid(Loomad):
    def Häälitsus(self):
        print("Huu huu")
        
jaagup=Mesilased()
priit=Kalad()
art=Sead()
vindu=Öökullid()

jaagup.Häälitsus()
priit.Häälitsus()
art.Häälitsus()
vindu.Häälitsus()