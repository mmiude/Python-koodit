# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus
# ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua
# parametreina saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class AutoLuokka:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka


auto1 = AutoLuokka("ABC-123", 142)

print(f"Reksiteritunnus: {auto1.rekisteritunnus}\nHuippunopeus: {auto1.huippunopeus} km/h\n"
      f"Hetkellinen nopeus: {auto1.nopeus} km/h\nKuljettu matka: {auto1.matka} km")
