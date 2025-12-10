class Auto:
    # Loome muutujad. Tegemist on antud juhul klassimuutujatega
    tootja = ""
    mudel = ""
    maxKiirus = 0
    maksumus =  0
    istekohtadeArv = 0
    hetkeKiirus = 0
    
    # Meetodi kirjeldamine algab def lausega. Pärast seda kirjeldame ära
    # meetodi nime. () vahel kirjeldame ära mitu ja mis sisendparameetrid me anname
    # NB! self tuleb alati meetodile kaasa. Selle abil saame me pöörduda
    # meetodi siseste struktuuride poole
    def valjastaAndmed(self):
        print("Tootja on:", self.tootja)
        print("Mudel on:", self.mudel)
        print("Hetke kiirus:", self.hetkeKiirus)
        print("Auto maksumus:", self.maksumus)
        print("Istekohtade arv:", self.istekohtadeArv)
        print("Maks kiirus:", self.maxKiirus)
        
    def vahendaKohtadearvu(self, mituKohta):
        if mituKohta > self.istekohtadeArv:
            print("Eemaldada ei saa rohkem kohti kui autos on.")
        else:
            self.istekohtadeArv -= mituKohta
            
    def kiirenda(self, kuiPalju):
        if self.hetkeKiirus + kuiPalju > self.maxKiirus:
            print("Saavutasin maksimaalse kiiruse, rohkem ei anna kiirendada.")
            self.hetkeKiirus = self.maxKiirus
        else:
            self.hetkeKiirus += kuiPalju
        # Ülesanne: Looge pidurda() meetod ka. Lähtuge eelnevalt tehtust
    def pidurda(self, kuiPalju):
        if self.hetkeKiirus - kuiPalju < 0:
            print("saavutasid minimaalse kiiruse, rohkem ei anna pidurdada")
            self.hetkeKiirus = 0
        else:
            self.hetkeKiirus = self.hetkeKiirus - kuiPalju
# Auto objekt
auto1 = Auto()
auto2 = Auto()

# Väärtustasin tootja andmeväljad nendes objektides
auto1.tootja = "BIMW"
auto2.tootja = "Blugarti"

# Täidan esimese auto teised andmed ka ära

auto1.mudel = "Ei mäleta"
auto1.maxKiirus = 1000
auto1.maksumus = 5
auto1.istekohtadeArv = 40
auto1.hetkeKiirus = 0
auto1.valjastaAndmed()

auto1.vahendaKohtadearvu(25)
auto1.valjastaAndmed()

auto1.kiirenda(1590)
auto1.valjastaAndmed()

# Täidan teise auto teised andmed ära

auto2.mudel = "roheline"
auto2.maxKiirus = 240
auto2.maksumus = 10000000000
auto2.istekohtadeArv = 2
auto2.hetkeKiirus = 100
auto2.valjastaAndmed()

auto2.pidurda(200)
auto2.valjastaAndmed()

