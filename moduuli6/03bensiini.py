# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän
# käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan
# siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän. Yksi gallona on 3,785 litraa.

def bensa_litroiksi (gallonat):
    litrat = gallonat * 3.785
    return litrat

gallonat = float(input("Anna gallonat: "))

while gallonat >= 0:
    print(f"{bensa_litroiksi(gallonat):.2f} litraa")
    gallonat = float(input("Anna gallonat: "))

print("Syötit negatiivisen luvun. Ohjelma päätetty.")