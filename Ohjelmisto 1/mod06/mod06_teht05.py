def suodata_parittomat(luvut):
   
    return [luku for luku in luvut if luku % 2 == 0]


def main():
    
    alkuperainen_lista = [3, 6, 7, 8, 1, 10, 5, 12]
    
    karsittu_lista = suodata_parittomat(alkuperainen_lista)
    
    print(f"Alkuperäinen lista: {alkuperainen_lista}")
    print(f"Karsittu lista (vain parilliset luvut): {karsittu_lista}")


if __name__ == "__main__":
    main()
