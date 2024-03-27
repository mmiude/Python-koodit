# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen
# julkaisun kaikki tiedot. Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6
# (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

from colorama import Fore
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"\n{Fore.LIGHTMAGENTA_EX}Kirjajulkaisut:{Fore.RESET}\nNimi: {self.nimi}\nKirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumäärä}")


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"\n{Fore.LIGHTMAGENTA_EX}Lehtijulkaisut:{Fore.RESET}\nNimi: {self.nimi}\nPäätoimittaja: {self.päätoimittaja}")


julkaisut = []

kirja1 = julkaisut.append(Kirja("Hytti no:o 6", "Rosa Liksom", 200))
lehti1 = julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))

for julkaisu in julkaisut:
    julkaisu.tulosta_tiedot()



