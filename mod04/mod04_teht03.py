luvut = []

while True:
    syote = input("Anna luku (tyhjä vastaus lopettaa): ")
    
    if syote == "":
        break
    
    luku = float(syote)
    luvut.append(luku)

if luvut:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Et syöttänyt yhtään lukua.")