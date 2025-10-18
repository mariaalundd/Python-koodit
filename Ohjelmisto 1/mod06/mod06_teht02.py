import random


def heita_noppaa(tahkot):
    return random.randint(1, tahkot)


def main():
    
    tahkot = int(input("Anna nopan tahkojen määrä: "))
    maksimi = int(input(f"Anna nopan maksimisilmäluku (1-{tahkot}): "))
    
    
    while True:
        silmaluku = heita_noppaa(tahkot)
        print(f"Sait silmäluvun: {silmaluku}")
        if silmaluku == maksimi:
            break

if __name__ == "__main__":
    main()
