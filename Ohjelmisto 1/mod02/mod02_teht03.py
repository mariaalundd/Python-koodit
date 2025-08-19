kanta_str = input("Anna suorakulmion kannan pituus: ")
kanta = float(kanta_str)
korkeus_str = input("Anna suorakulmion korkeus: ")
korkeus = float(korkeus_str)
alue = kanta*korkeus
piiri = kanta+kanta+korkeus+korkeus
print("Suorakulmion pinta-ala: " + str(alue))
print("Suorakulmion piiri: " + str(piiri))