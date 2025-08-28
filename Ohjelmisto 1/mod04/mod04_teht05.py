oikea_tunnus = "python"
oikea_salasana = "rules"

max_yritykset = 5
yritykset = 0

while yritykset < max_yritykset:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    
    else:
        yritykset += 1
        print(f"Väärä tunnus tai salasana. Yrityksiä jäljellä: {max_yritykset - yritykset}")

else:
    print("Pääsy evätty.")