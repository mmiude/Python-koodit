sukupuoli = input("Kerro biologinen sukupuoli: ")
hemoglobiini = int(input("Anna hemoglobiini arvo (g/l): "))
if sukupuoli == "nainen" and 117 <= hemoglobiini <= 175 or sukupuoli == "mies" and 134 <= hemoglobiini <= 195:
    print("Hemoglobiiniarvo normaali.")
elif sukupuoli == "nainen" and hemoglobiini < 117 or sukupuoli == "mies" and hemoglobiini < 134:
    print("Hemoglobiiniarvo on alhainen.")
else: print("Hemoglobiiniarvo on korkea.")


