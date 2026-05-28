kaupungit = []

for i in range(5):
    nimi = input(f"Anna {i+1}. kaupungin nimi: ")
    kaupungit.append(nimi)

print("Syöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)