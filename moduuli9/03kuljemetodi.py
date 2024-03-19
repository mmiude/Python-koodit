# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class AutoLuokka:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka = self.matka + tunnit * self.nopeus


auto1 = AutoLuokka("ABC-123", 142)

auto1.kiihdytä(30)
auto1.kulje(1)
auto1.kiihdytä(70)
auto1.kulje(0.5)
auto1.kiihdytä(50)
auto1.kulje(1)
print(f"Hetkellinen nopeus: {auto1.nopeus} km/h\nKuljettu matka: {auto1.matka} km")

auto1.kiihdytä(-200)
print(f"Hetkellinen nopeus: {auto1.nopeus} km/h")