# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä
# 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def nopan_heitto():
    heitto = random.randint(1,6)
    return heitto

nopan_luku = nopan_heitto()

while nopan_luku != 6:
    print(f"Sait: {nopan_luku}")
    nopan_heitto()
    nopan_luku = nopan_heitto()

print("Sait kutosen! Peli loppu!")




