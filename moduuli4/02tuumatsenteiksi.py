tuumat = float(input("Anna tuumat: "))
while tuumat >= 0:
    tuumat_senteiksi = tuumat * 2.54
    print(f"Sentteinä: {tuumat_senteiksi}cm")
    tuumat = float(input("Anna tuumat: "))
print("Ohjelma lopetettu.")
