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