# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa
# olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja
# tulostat sen palauttaman summan.

def lista_summana(lista):
    summa = sum(lista)
    return summa

lista = [1, 21, 4, 6, 7]

print(f"listan luvut yhteensä: {lista_summana(lista)}")