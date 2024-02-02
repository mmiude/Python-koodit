# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan
# hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza
# antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

def unit_price(halkaisija, hinta):
    halkaisija_met = halkaisija / 100
    unit_price = hinta / halkaisija_met
    return unit_price


pizza1_halkaisija = float(input("Anna pizza nro 1 halkaisija (cm): "))
pizza1_hinta = float(input("Anna pizza nro 1 hinta euroina: "))

pizza2_halkaisija = float(input("Anna pizza nro 2 halkaisija (cm): "))
pizza2_hinta = float(input("Anna pizza nro 2 hinta euroina: "))

tulos1 = unit_price(pizza1_halkaisija, pizza1_hinta)
tulos2 = unit_price(pizza2_halkaisija, pizza2_hinta)

if tulos1 > tulos2:
    print(f"Pizza nro 2 on edullisempi yksikköhinnalla: {tulos2:.2f} €/m²\nPizzan nro 1 yksikköhinta: {tulos1:.2f} €/m²")
elif tulos1 == tulos2:
    print("Pizzojen yksikköhinnat ovat samat!")
else:
    print(f"Pizza nro 1 on edullisempi yksikköhinnalla: {tulos1:.2f} €/m²\nPizzan nro 2 yksikköhinta: {tulos2:.2f} €/m²")

