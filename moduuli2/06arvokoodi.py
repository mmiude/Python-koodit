import random
n1 = random.randint(0,9)
n2 = random.randint(0,9)
n3 = random.randint(0,9)
koodi1 = n1 *100 + n2 *10 + n3
n_1 = random.randint(0,9)
n_2 = random.randint(0,9)
n_3 = random.randint(0,9)
koodi2 = n_1 *100 + n_2 * 10 + n_3
while koodi2 == koodi1:
    n_1 = random.randint(0, 9)
    n_2 = random.randint(0, 9)
    n_3 = random.randint(0, 9)
    koodi2 = n_1 * 100 + n_2 * 10 + n_3
print(f"Ensimmäinen koodi: {koodi1}\n" + f"Toinen koodi: {koodi2}")
numero1 = random.randint(1, 6)
numero2 = random.randint(1, 6)
numero3 = random.randint(1, 6)
numero4 = random.randint(1, 6)
koodi_1 = numero1 * 1000 + numero2 *100 + numero3 *10 + numero4
numero_1 = random.randint(1, 6)
numero_2 = random.randint(1, 6)
numero_3 = random.randint(1, 6)
numero_4 = random.randint(1, 6)
koodi_2 = numero_1 * 1000 + numero_2 * 100 + numero_3 * 10 + numero_4
while koodi_2 == koodi_1:
    numero_1 = random.randint(1, 6)
    numero_2 = random.randint(1, 6)
    numero_3 = random.randint(1, 6)
    numero_4 = random.randint(1, 6)
    koodi_2 = numero_1 * 1000 + numero_2 * 100 + numero_3 * 10 + numero_4
print(f"Esimmäinen koodi: {koodi_1}\n" + f"Toinen koodi: {koodi_2}")