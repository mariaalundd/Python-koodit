käyttäjä = input('Anna nimesi: ')
print("Terve, " + käyttäjä + "!")

säde_str = input("Anna ympyrän säde: ")
säde = float(säde_str)
alue = 3.14159265*säde**2
print("Ympyrän pinta-ala: " + str(alue))

kanta_str = input("Anna suorakulmion kannan pituus: ")
kanta = float(kanta_str)
korkeus_str = input("Anna suorakulmion korkeus: ")
korkeus = float(korkeus_str)
alue = kanta*korkeus
piiri = kanta+kanta+korkeus+korkeus
print("Suorakulmion pinta-ala: " + str(alue))
print("Suorakulmion piiri: " + str(piiri))

luku1_str = input("Anna yksi kokonaisluku: ")
luku1 = float(luku1_str)
luku2_str = input("Anna toinen kokonaisluku: ")
luku2 = float(luku2_str)
luku3_str = input("Anna kolmas kokonaisluku: ")
luku3 = float(luku3_str)
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3)//3
print("Lukujen summa: " + str(summa))
print("Lukujen tulo: " + str(tulo))
print("Lukujen keskiarvo: " + str(keskiarvo))

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
leiviskat_nauloina = 20
naulat_luoteina = 32
luodit_grammoina = 13.3
kokonaisluodit = float(leiviskat * leiviskat_nauloina * naulat_luoteina) + (naulat * naulat_luoteina) + luodit
kokonaispaino = float(kokonaisluodit * luodit_grammoina)
kilot = float(kokonaispaino // 1000)
grammat = kokonaispaino % 1000
print("Massa nykymittojen mukaan:")
print(f"{kilot:.0f} kilogrammaa ja {grammat:.2f} grammaa")

