# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
# mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()

uusi_nimi = input("Anna nimi: ")

while uusi_nimi != "":
    if uusi_nimi not in nimet:
        nimet.add(uusi_nimi)
        print(f"{uusi_nimi} on uusi nimi!")
        uusi_nimi = input("Anna uusi nimi: ")

    if uusi_nimi in nimet:
        print(f"{uusi_nimi} on aiemmin syötetty!")
        uusi_nimi = input("Anna uusi nimi: ")


print("Ohjelma lopetettu. Nimet listattuna: ")

for nimi in nimet:
    print(nimi)