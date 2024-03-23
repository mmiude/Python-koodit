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

    def __init__(self, ground_floor, top_floor, lifts):
        self.ground_floor = ground_floor
        self.top_floor = top_floor
        self.lifts = []
        for i in range (lifts):
            self.lifts.append(Lift(ground_floor, top_floor))

    def move_lift(self, lift_number, new_floor):
        self.lifts[lift_number-1].move_to(new_floor)
        print(f"Lift number {lift_number} has been moved to {new_floor} floor")

    def fire_alarm(self):
        for i in range(len(self.lifts)):
            self.lifts[i].move_to(0)
        print(f"Fire alarm. Lifts has been moved to the ground floor")
        for lift in self.lifts:
            print(f"{lift.current_floor}")


house1 = House(0, 10, 4)
house1.move_lift(2, 4)
house1.move_lift(3, 6)
house1.move_lift(1, 4)
house1.move_lift(4, 6)
house1.fire_alarm()

for lift in house1.lifts:
    print(lift.current_floor, lift.ground_floor, lift.top_floor)

