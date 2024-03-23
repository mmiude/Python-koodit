# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja
# ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin
# numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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


class House:
    lift_list = []

    def __init__(self, ground_floor, top_floor, lifts):
        self.ground_floor = ground_floor
        self.top_floor = top_floor
        for i in range(lifts):
            House.lift_list.append(Lift(ground_floor, top_floor))
        self.lift_list = House.lift_list

    def move_lift(self, lift_number, new_floor):
        House.lift_list[lift_number-1].move_to(new_floor)


lift1 = Lift(0, 10)
lift1.move_to(8)
lift1.move_to(0)

house1 = House(0, 10, 2)
house1.move_lift(2, 4)


