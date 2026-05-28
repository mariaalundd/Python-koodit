luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luvut.append(int(syote))

luvut.sort(reverse=True)

viisi_suurinta = luvut[:5]

print("Viisi suurinta lukua:", viisi_suurinta)