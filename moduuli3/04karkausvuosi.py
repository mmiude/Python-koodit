vuosiluku = int(input("Anna vuosiluku: "))
if vuosiluku % 4 == 0 and vuosiluku % 100 == vuosiluku % 400:
    print("Nyt on karkausvuosi.")
else: print("Nyt ei ole karkausvuosi.")