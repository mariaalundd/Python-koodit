while True:
    tuumat = float(input("Anna tuumamäärä: "))
    
    if tuumat < 0:
        print("Negatiivinen luku ei kelpaa.")
        break
    
    tuuma_cm = 2.54
    cm = tuumat * tuuma_cm
    print(f"{tuumat} tuumaa = {cm} cm")