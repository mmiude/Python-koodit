import random
n1 = str(random.randint(0,9))
n2 = str(random.randint(0,9))
n3 = str(random.randint(0,9))
koodi1 = n1 + n2 + n3
n_1 = str(random.randint(0,9))
n_2 = str(random.randint(0,9))
n_3 = str(random.randint(0,9))
koodi2 = n_1 + n_2 + n_3
while koodi2 == koodi1:
    n_1 = str(random.randint(0, 9))
    n_2 = str(random.randint(0, 9))
    n_3 = str(random.randint(0, 9))
    koodi2 = n_1 + n_2 + n_3
print(f"Ensimmäinen koodi: {koodi1}\n" + f"Toinen koodi: {koodi2}")
numero1 = str(random.randint(1, 6))
numero2 = str(random.randint(1, 6))
numero3 = str(random.randint(1, 6))
numero4 = str(random.randint(1, 6))
koodi_1 = numero1 + numero2 + numero3 + numero4
numero_1 = str(random.randint(1, 6))
numero_2 = str(random.randint(1, 6))
numero_3 = str(random.randint(1, 6))
numero_4 = str(random.randint(1, 6))
koodi_2 = numero1 + numero2 + numero3 + numero4
while koodi_2 == koodi_1:
    numero_1 = str(random.randint(1, 6))
    numero_2 = str(random.randint(1, 6))
    numero_3 = str(random.randint(1, 6))
    numero_4 = str(random.randint(1, 6))
    koodi_2 = numero_1 + numero_2 + numero_3 + numero_4
print(f"Esimmäinen koodi: {koodi_1}\n" + f"Toinen koodi: {koodi_2}")