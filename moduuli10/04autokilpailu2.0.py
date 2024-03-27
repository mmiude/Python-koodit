# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
# pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen,
# kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
        #* tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
        # eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
        #* tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
        #* kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
        # kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle annetaan
# kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla
# toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen,
# kun kilpailu on päättynyt.

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


class Kilpailu():
    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autolista = autolista

    def tunti_kuluu(self):
        for auto in self.autolista:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)


    def tulosta_tilanne(self):
        for auto in self.autolista:
            print(f"{Fore.LIGHTMAGENTA_EX}Rekkari: {Fore.LIGHTCYAN_EX}{auto.rekisteritunnus:6s} "
                f"{Fore.LIGHTMAGENTA_EX}Huippunopeus: {Fore.LIGHTCYAN_EX}{auto.huippunopeus:3d} km/h  "
                f"{Fore.LIGHTMAGENTA_EX}Nopeus: {Fore.LIGHTCYAN_EX}{auto.nopeus:3d} km/h  "
                f"{Fore.LIGHTMAGENTA_EX}Matka: {Fore.LIGHTCYAN_EX}{auto.matka} km{Fore.RESET}")

    def kilpailu_ohi(self):
        matkat = []
        for auto in self.autolista:
            matkat.append(auto.matka)
        if max(matkat) >= self.pituus:
            return True
        else:
            return False


autot = []

for i in range(10):
    nopeus = random.randint(100, 200)
    reksiteritunnus = f"ABC-{i + 1}"
    autot.append(AutoLuokka(reksiteritunnus, nopeus))

suuri_romuralli = Kilpailu("Suuri Romuralli", 8000, autot)


while not suuri_romuralli.kilpailu_ohi():
    for i in range(10):
        if suuri_romuralli.kilpailu_ohi():
            break
        suuri_romuralli.tunti_kuluu()
    print(80*"-"+"\n10h kulunut. Väliaikatulokset:")
    suuri_romuralli.tulosta_tilanne()
    print(80*"-")


print(80*"-" + "\nKilpailu on päättynyt. Tulokset:")
suuri_romuralli.tulosta_tilanne()
print(80*"-")




