# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
# haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta
# kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

lentoasema_tiedot = {}

user_input = input("Haluatko lisätä tai hakea lentoaseman vai lopettaa ohjelman (komennot: lisää/hae/lopeta)? ")

while True:
    if user_input == "lisää":
        icao_code = input("Anna lentoaseman ICAO-koodi: ")
        airport_name = input("Anna lentoaseman nimi: ")
        lentoasema_tiedot[icao_code] = airport_name
        user_input = input("Haluatko lisätä, hakea vai lopettaa? ")
    if user_input == "hae":
        icao_code_search = input("Anna ICAO-koodi: ")
        if icao_code_search in lentoasema_tiedot:
            print(f"Lentoaseman nimi: {lentoasema_tiedot[icao_code_search]}")
        else:
            print("Lentokenttää ei löytynyt.")
        user_input = input("Haluatko lisätä, hakea vai lopettaa ")
    if user_input == "lopeta":
        print("Ohjelma lopetettu.")
        break



