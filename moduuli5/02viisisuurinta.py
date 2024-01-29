list = []

luku = int(input("Anna luku: "))
while luku != "" :
    list.append(luku)
    luku = input("Anna seuraava luku tai paina Enter lopettaaksesi: ")
    if luku.strip():
        luku = int(luku)
list.sort(reverse=True)
print(f"Viisi suurinta numeroa: {list[:5]}")
