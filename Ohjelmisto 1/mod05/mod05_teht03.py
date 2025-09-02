numero = int(input("Anna kokonaisluku: "))

if numero < 2:
    print(f"Luku {numero} ei ole alkuluku.")
else:
    on_alkuluku = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print(f"Luku {numero} on alkuluku.")
    else:
        print(f"Luku {numero} ei ole alkuluku.")