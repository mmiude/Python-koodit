import random

list = []
arpakuutiot = int(input("Anna arpakuutioiden määrä: "))

for arpakuutio in range(arpakuutiot):
    list.append(random.randint(1,6))

summa = sum(list)
print(list)
print(f"Silmälukujen yhteenlaskettu summa: {summa}")


