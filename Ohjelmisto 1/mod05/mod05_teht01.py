import random

nopat = int(input("Anna heitettävien noppien määrä: "))

summa = 0
for i in range(nopat):
    silmaluku = random.randint(1, 6)
    summa += silmaluku

print("Silmälukujen summa: ", summa)