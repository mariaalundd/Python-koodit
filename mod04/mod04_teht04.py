import random

oikea_luku = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku (1-10): "))
    
    if arvaus < oikea_luku:
        print("Liian pieni arvaus.")
    elif arvaus > oikea_luku:
        print("Liian suuri arvaus.")
    elif arvaus == oikea_luku:
        print("Oikein! Arvasit luvun.")
        break