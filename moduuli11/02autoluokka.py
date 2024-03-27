# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on
# bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan
# rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun
# asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton
# (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle
# haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

import random
from colorama import Fore


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

    def tulokset(self):
        print(f"{Fore.LIGHTMAGENTA_EX}Rekkari: {Fore.LIGHTCYAN_EX}{self.rekisteritunnus:6s} "
              f"{Fore.LIGHTMAGENTA_EX}Huippunopeus: {Fore.LIGHTCYAN_EX}{self.huippunopeus:3d} km/h  "
              f"{Fore.LIGHTMAGENTA_EX}Nopeus: {Fore.LIGHTCYAN_EX}{self.nopeus:3d} km/h  "
              f"{Fore.LIGHTMAGENTA_EX}Matka: {Fore.LIGHTCYAN_EX}{self.matka} km{Fore.RESET}")

class SähköAuto(AutoLuokka):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, nopeus=0, matka=0):
        super().__init__(rekisteritunnus, huippunopeus, nopeus, matka)
        self.akkukapasiteetti = akkukapasiteetti


class PolttomoottoriAuto(AutoLuokka):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki, nopeus=0, matka=0):
        super().__init__(rekisteritunnus, huippunopeus, nopeus, matka)
        self.bensatankki = bensatankki




autot = []

sähköauto1 = autot.append(SähköAuto("ABC-15", 180, 52.5))
polttoauto1 = autot.append(PolttomoottoriAuto("ABC-123", 165, 32.3))

autot[0].kiihdytä(120)
autot[1].kiihdytä(100)

for auto in autot:
    auto.kulje(3)
    auto.tulokset()







