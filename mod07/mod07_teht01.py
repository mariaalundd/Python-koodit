vuodenajat = (
    "talvi", "talvi", "kevät",  # tammi, helmi, maalis
    "kevät", "kevät", "kesä",   # huhti, touko, kesä
    "kesä", "kesä", "syksy",    # heinä, elo, syys
    "syksy", "syksy", "talvi"   # loka, marras, joulu
)


def main():
    kuukausi = int(input("Anna kuukauden numero (1-12): "))
    if 1 <= kuukausi <= 12:
        vuodenaika = vuodenajat[kuukausi - 1]
        print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan: {vuodenaika}.")
    else:
        print("Virheellinen kuukauden numero! Anna luku väliltä 1-12.")


if __name__ == "__main__":
    main()
