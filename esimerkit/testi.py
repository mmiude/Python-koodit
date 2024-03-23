class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tervehdys(self):
        print(f"Moi nimeni on {self.name} ja ikäni on {self.age} ")

class Student(Person):
    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number

    def tervehdys(self):
        super().tervehdys()
        print(f"Mun opiskelijanumero on {self.number}")


person1 = Person("Pekka", 20)
student1 = Student("Sara", 22, 123)

student1.tervehdys()


























