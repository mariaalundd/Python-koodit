sukupuoli = input("Anna sukupuoli (nainen/mies): ").lower()
hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiini on alhainen.")
    elif 117 <= hemoglobiini <= 175:
        print("Hemoglobiini on normaali.")
    else:
        print("Hemoglobiini on korkea.")
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiini on alhainen.")
    elif hemoglobiini > 195:
        print("Hemoglobiini on korkea.")
    else:
        print("Hemoglobiini on normaali.")
else:
    print("Virheellinen sukupuoli.")