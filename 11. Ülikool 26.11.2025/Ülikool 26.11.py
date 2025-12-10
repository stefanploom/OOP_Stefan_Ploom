class Teaduskond:
    def __init__(self, nimi, juhataja):
        self.nimi = nimi
        self.juhataja = juhataja
        self.tudengid = []
        
    def lisa_tudeng(self, tudeng):
        self.tudengid.append(tudeng)
        
    def ValjastaAndmed(self):
        print(f"Teaduskond: {self.nimi}, Juhataja: {self.juhataja}")
        for tudeng in self.tudengid:
            print(f"Tudeng: {tudeng.nimi}, Õppeaste: {tudeng.õppeaste}, Teaduskond: {tudeng.teaduskond.nimi}")
        
class Tudeng:
    def __init__(self, nimi, tudengikood, õppeaste, teaduskond):
        self.nimi = nimi
        self.tudengikood = tudengikood
        self.õppeaste = õppeaste
        self.teaduskond = teaduskond

class BakalaureuseTudeng(Tudeng):
    def __init__(self, nimi, kood, teaduskond, lõputööteema):
        super().__init__(nimi, kood, "Bakalaureus", teaduskond)
    
class MagistriTudeng(Tudeng):
    def __init__(self, nimi, kood, teaduskond, juhataja):
        super().__init__(nimi, kood, "Bakalaureus", teaduskond)
        self.juhataja = juhataja
    
tk1 = Teaduskond("Lugemine", "Mandem Aamens")
tk2 = Teaduskond("Arenenud Arvamine", "Midag Gi. Sello")
tk3 = Teaduskond("Käekirja Dešifreerimine", "Hr. Viilo")

t1 = BakalaureuseTudeng("Art-Robin Afanasjev", "18257", tk1, "Aabits")
t2 = BakalaureuseTudeng("Plipu Ploppu", "89620", tk1, "Paber")
t3 = MagistriTudeng("Muhv", "18257", tk1, "Herman Lukk")

t4 = BakalaureuseTudeng("Freddy Pais", "87269", tk2, "Raske küsimus")
t5 = BakalaureuseTudeng("Stefan Ploom", "54156", tk2, "Suur arvamus")
t6 = MagistriTudeng("Afanasjev-Robin Art", "75281", tk2, "")

t7 = BakalaureuseTudeng("Suvakas Vend", "17584", tk3, "Õpilaste käekiri")
t8 = BakalaureuseTudeng("Ilmus Maale", "90872", tk3, "Hieroglüüfid")
t9 = MagistriTudeng("Malma LAN", "65721", tk3, "Sammalhabe")

tk1.lisa_tudeng(t1)
tk1.lisa_tudeng(t2)
tk1.lisa_tudeng(t3)

tk2.lisa_tudeng(t4)
tk2.lisa_tudeng(t5)
tk2.lisa_tudeng(t6)

tk3.lisa_tudeng(t7)
tk3.lisa_tudeng(t8)
tk3.lisa_tudeng(t9)

tk1.ValjastaAndmed()
tk2.ValjastaAndmed()
tk3.ValjastaAndmed()



