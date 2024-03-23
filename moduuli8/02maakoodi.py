# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä
# maassa olevien lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava
# tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector
def lentokenttien_lukumäärät_tyypeittäin(iso_country):
    sql = f"SELECT type, COUNT(*) as rivejä FROM airport WHERE iso_country = '{iso_country}' group by type;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    # print(tulos)
    for tulo in tulos:
        if "small_airport" in tulo:
            print(f"Pieniä kenttiä: {tulo[1]} kpl")
        if "medium_airport" in tulo:
            print(f"Keskikokoisa kenttiä: {tulo[1]} kpl")
        if "large_airport" in tulo:
            print(f"Isoja kenttiä: {tulo[1]} kpl")
        if "heliport" in tulo:
            print(f"Helikoperikenttiä: {tulo[1]} kpl")
        if "balloonport" in tulo:
            print(f"Balloonportteja: {tulo[1]} kpl")
        if "seaplane_base" in tulo:
            print(f"Vesilentokonekenttiä: {tulo[1]} kpl")
        if "closed" in tulo:
            print(f"Suljettuja kenttiä: {tulo[1]} kpl")


yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

iso_country = input("Anna maakoodi: ")
lentokenttien_lukumäärät_tyypeittäin(iso_country)
