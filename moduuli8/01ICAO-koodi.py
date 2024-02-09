# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja
# tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

def hae_lentokenttä_icao_koodilla(icao_koodi):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao_koodi}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän nimi: {rivi[0]}, sijaintikunta: {rivi[1]}")
    return

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

icao_koodi = input("Anna ICAO-koodi: ")
hae_lentokenttä_icao_koodilla(icao_koodi)
