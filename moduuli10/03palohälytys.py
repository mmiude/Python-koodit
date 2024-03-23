# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

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
            print(f"Lift has been moved to {self.current_floor} floor")
        if new_floor < self.current_floor:
            floor_difference = self.current_floor - new_floor
            for i in range(floor_difference):
                self.floor_down()
            print(f"Lift has been moved to {self.current_floor} floor")

    def floor_up(self):
        self.current_floor = self.current_floor + 1

    def floor_down(self):
        self.current_floor = self.current_floor - 1


class House:

    def __init__(self, ground_floor, top_floor, lifts):
        self.ground_floor = ground_floor
        self.top_floor = top_floor
        self.lifts = []
        for i in range(lifts):
            self.lifts.append(Lift(ground_floor, top_floor))

    def move_lift(self, lift_number, new_floor):
        print(f"Moving lift number {lift_number} to the {new_floor} floor:")
        self.lifts[lift_number-1].move_to(new_floor)

    def fire_alarm(self):
        print(f"Fire alarm. Lifts have been moved to the ground floor. Double check that all {len(self.lifts)} "
              f"lifts are on the ground floor:")
        for i in range(len(self.lifts)):
            self.lifts[i].move_to(0)


house1 = House(0, 10, 4)
house1.move_lift(2, 4)
house1.move_lift(3, 6)
house1.move_lift(1, 4)
house1.move_lift(4, 6)
house1.fire_alarm()


