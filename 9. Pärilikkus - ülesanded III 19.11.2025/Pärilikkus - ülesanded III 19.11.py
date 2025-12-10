from abc import ABC, abstractmethod
import random


class Karakter(ABC):
    def __init__(self, nimi, hp, tugevus):
        self.nimi = nimi
        self.hp = hp
        self.tugevus = tugevus

    @abstractmethod
    def runnak(self, sihtmärk):
        print(f"{self.nimi} sooritab rünnaku!")

    def kas_on_elus(self):
        return self.hp > 0

    def vigastus(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        print(f"{self.nimi} sai {dmg} kahju! (HP: {self.hp})")



class Warrior(Karakter):

    def runnak(self, sihtmärk):
        print(f"{self.nimi} virutab mõõgaga!")
        dmg = self.tugevus

        if random.random() < 0.30:
            dmg = int(dmg * 0.5)
            print(f"⚔️ {self.nimi} tegi nõrgema rünnaku (blokk aktiveerus)")

        sihtmärk.vigastus(dmg)


class Archer(Karakter):

    def runnak(self, sihtmärk):
        print(f"{self.nimi} laseb noole!")
        dmg = self.tugevus

        if random.random() < 0.20:
            dmg *= 2
            print(f"🎯 KRIIT! {self.nimi} teeb topeltkahju!")

        sihtmärk.vigastus(dmg)


class Mage(Karakter):

    def runnak(self, sihtmärk):
        print(f"{self.nimi} viskab tulepalli!")
        dmg = self.tugevus

        if random.random() < 0.20:
            heal = random.randint(5, 15)
            self.hp += heal
            print(f"✨ {self.nimi} ravib ennast {heal} HP võrra! (HP: {self.hp})")

        sihtmärk.vigastus(dmg)



class Areena:

    def __init__(self, char1, char2, char3):
        self.osalejad = [char1, char2, char3]

    def võitlus(self):
        print("\n=== VÕITLUS ALGAB! ===\n")
        round_nr = 1

        while sum(c.kas_on_elus() for c in self.osalejad) > 1:

            print(f"\n----- ROUND {round_nr} -----")

            elus_list = [c for c in self.osalejad if c.kas_on_elus()]

            for ründaja in elus_list:

                if not ründaja.kas_on_elus():
                    continue

                sihtide_hulgast = [c for c in self.osalejad if c != ründaja and c.kas_on_elus()]
                if not sihtide_hulgast:
                    break

                sihtmärk = random.choice(sihtide_hulgast)

                print(f"\n{ründaja.nimi} ründab -> {sihtmärk.nimi}")
                ründaja.runnak(sihtmärk)
            print("\nHP seis peale roundi:")
            for c in self.osalejad:
                print(f"{c.nimi}: {c.hp} HP")

            round_nr += 1

        print("\n=== VÕITLUS LÄBI! ===")
        for c in self.osalejad:
            if c.kas_on_elus():
                print(f"🏆 Võitja on: {c.nimi} (HP: {c.hp})")
                return



sõdalane = Warrior("Ertd", 200, 22)
vibukütt = Archer("Kirk", 160, 19)
võlur = Mage("Adern", 190, 25)

areena = Areena(sõdalane, vibukütt, võlur)
areena.võitlus()