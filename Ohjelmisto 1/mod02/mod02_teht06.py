import random

koodi1 = [random.randint(0, 9) for _ in range(3)]
koodi2 = [random.randint(1, 6) for _ in range(4)]
print("Kolminumeroinen koodi (0–9):", koodi1)
print("Nelinumeroinen koodi (1–6):", koodi2)

koodi3 = "".join(str(random.randint(0, 9)) for _ in range(3))
koodi4 = "".join(str(random.randint(1, 6)) for _ in range(4))
print("Kolminumeroinen koodi (0–9):" + koodi3)
print("Nelinumeroinen koodi (1–6):" + koodi4)

