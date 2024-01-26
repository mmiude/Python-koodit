import random
#alustetaan pisteiden lukumäärälaskurit

N = n = 0

arvottavat_pisteet = float(input("Arvottavat pisteet: "))

while N < arvottavat_pisteet:
#arvotaan yksi piste
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    N += 1
    print(f"Arvottu piste: {x}, {y}")
    if x * x + y * y < 1:
        n += 1
print(f"Pisteitä yhteensä: {N}, joista ympyrän sisällä {n}.")
# lasketaan piin likiarvo
piin_likiarvo = 4 * n / N
print(f"Piin likiarvo on {piin_likiarvo}")