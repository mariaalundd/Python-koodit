import sqlite3

def hae_lentokentta(icao_koodi):
  
    conn = sqlite3.connect('lentokentat.db')
    cursor = conn.cursor()

  
    cursor.execute("""
        SELECT name, municipality 
        FROM airport 
        WHERE ident = ?
    """, (icao_koodi.upper(),))  

    tulos = cursor.fetchone()
    conn.close()

    if tulos:
        nimi, kunta = tulos
        print(f"Lentokenttä: {nimi}\nSijaintikunta: {kunta}")
    else:
        print("Lentokenttää ei löytynyt annetulla ICAO-koodilla.")

def main():
    icao = input("Anna lentoaseman ICAO-koodi: ")
    hae_lentokentta(icao)

if __name__ == "__main__":
    main()