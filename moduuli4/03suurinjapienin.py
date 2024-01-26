# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

#suurin ja pienin
suurin_luku = float("-inf")
pienin_luku = float("inf")

while True:
    luku = input("Anna numero: ")
    if luku.strip():
        luku_int = int(luku)
        if luku_int > suurin_luku:
            suurin_luku = luku_int
        if luku_int < pienin_luku:
            pienin_luku = luku_int
    if luku == "":
        print(f"Ohjelma lopetettu. Suurin luku {suurin_luku} ja pienin luku {pienin_luku}.")
        break










