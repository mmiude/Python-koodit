# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

user = "python"
password = "rules"
attempts = 0

while attempts <= 5:
    ask_user = input("Anna käyttäjätunnus: ")
    ask_password = input("Anna salasana: ")

    if ask_user == user and ask_password == password:
        print("Tervetuloa!")
        break
    if ask_user != user and ask_password != password:
        print("Väärä käyttäjätunnus tai salasana!")
        attempts += 1
    if attempts == 5:
        print("Pääsy evätty!")
        break












