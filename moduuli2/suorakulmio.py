kanta_str = input("Syötä kanta: ")
kanta = float(kanta_str)
korkeus_str = input("Syötä korkeus: ")
korkeus = float(korkeus_str)
pinta_ala = kanta * korkeus
piiri = kanta * 2 + korkeus * 2
print(f"suorakulmion pinta ala: {pinta_ala:.2f}" + f"\nsuorakulmion piiri: {piiri:.2f}")

