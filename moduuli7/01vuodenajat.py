# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa
# sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat
# vuodenajat merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden
# mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausi = int(input("Anna kuukauden numero (1-12): "))

vuodenaika = vuodenajat[kuukausi-1]

print(f"Nyt on: {vuodenaika}")




