# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai
# kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat
# hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa
# siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen
# ja sen jälkeen takaisin alimpaan kerrokseen.

class Lift:
    def __init__(self, ground_floor, top_floor):
        self.ground_floor = ground_floor
        self.top_floor = top_floor
        self.current_floor = ground_floor

    def move_to(self, new_floor):
        if new_floor > self.current_floor:  # tarkistetaan mennäänkö ylös
            floor_difference = new_floor - self.current_floor  # lasketaan kuinka monta kerrosta on liikuttava
            for i in range(floor_difference):  # kutsutaan floor_up funktiota yllä lasketun erotuksen verran
                self.floor_up()
            print(f"You're now on the {self.current_floor} floor")
        if new_floor < self.current_floor:
            floor_difference = self.current_floor - new_floor
            for i in range(floor_difference):
                self.floor_down()
            print(f"You're now on the {self.current_floor} floor")

    def floor_up(self):
        self.current_floor = self.current_floor + 1

    def floor_down(self):
        self.current_floor = self.current_floor - 1


lift1 = Lift(0, 10)
lift1.move_to(8)
lift1.move_to(0)

