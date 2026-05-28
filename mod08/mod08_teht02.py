import sqlite3

def laske_lentokentat_maakoodilla(maakoodi):
  
    conn = sqlite3.connect('lentokentat.db')
    cursor = conn.cursor()

 
    cursor.execute("""
        SELECT type, COUNT(*) 
        FROM airport 
        WHERE iso_country = ?
        GROUP BY type
    """, (maakoodi.upper(),))

    tulokset = cursor.fetchall()
    conn.close()

    if tulokset:
        print(f"Lentokenttien määrät maassa '{maakoodi.upper()}':")
        for tyyppi, maara in tulokset:
            print(f"- {tyyppi}: {maara} kpl")
    else:
        print(f"Lentokenttiä ei löytynyt maasta '{maakoodi.upper()}'.")

def main():
    maakoodi = input("Anna maan ICAO-koodi (esim. FI): ")
    laske_lentokentat_maakoodilla(maakoodi)

if __name__ == "__main__":
    main()