# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random
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
        print(f"Rekkari: {self.rekisteritunnus:6s}  Huippunopeus: {self.huippunopeus:3d} km/h  Nopeus: {self.nopeus:3d} km/h  Matka: {self.matka} km")


autot = []

for i in range(10):
    nopeus = random.randint(100, 200)
    reksiteritunnus = f"ABC-{i+1}"
    autot.append(AutoLuokka(reksiteritunnus, nopeus))

#for auto in autot:
    #print(f"Rekkari: {auto.rekisteritunnus} huippunopeus: {auto.huippunopeus} km/h)

while True:
    matkat = []
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        matkat.append(auto.matka)
    if max(matkat) >= 1000:
        break


for auto in autot:
    auto.tulokset()
    print(80*"-")









