# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta
# haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy
# ja vie asennus loppuun.

import mysql.connector
from geopy import distance
def lentokenttien_etäisyys(icao_koodi1, icao_koodi2):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao_koodi1}' OR ident = '{icao_koodi2}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    sijainti1 = tulos[0]
    sijainti2 = tulos[1]
    etäisyys = distance.distance(sijainti1, sijainti2).km
    print(f"Lentokenttien välinen etäisyys: {etäisyys:.2f}km")
    return

yhteys=mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

icao_koodi1 = input("Anna ensimmäinen ICAO-koodi: ")
icao_koodi2 = input("Anna toinen ICAO-koodi: ")
lentokenttien_etäisyys(icao_koodi1, icao_koodi2)