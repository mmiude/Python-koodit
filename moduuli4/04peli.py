# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus
# tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

tietokoneen_luku = random.randint(1, 10)
arvattu_luku = int(input("Arvaa luku 1-10 välistä: "))

while arvattu_luku != tietokoneen_luku:
    if arvattu_luku < tietokoneen_luku:
        print("Liian pieni luku.")
        arvattu_luku = int(input("Arvaa uudelleen: "))
    if arvattu_luku > tietokoneen_luku:
        print("Liian suuri luku.")
        arvattu_luku = int(input("Arvaa uudelleen: "))
    if arvattu_luku == tietokoneen_luku:
        break

if arvattu_luku == tietokoneen_luku:
    print("Arvasit oikein! 💫")

