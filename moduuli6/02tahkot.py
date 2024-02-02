# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def nopan_heitto(tahkot):
    heitto = random.randint(1,tahkot)
    return heitto

tahkot = int(input("Anna nopan tahkojen määrä: "))
nopan_luku = nopan_heitto(tahkot)


while nopan_luku != tahkot:
    print(f"Sait: {nopan_luku}")
    nopan_heitto(tahkot)
    nopan_luku = nopan_heitto(tahkot)

print(f"Sait {tahkot}! Peli loppu!")