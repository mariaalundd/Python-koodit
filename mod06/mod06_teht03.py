def gallona_litroiksi(gallona):
    return gallona * 3.785


def main():
    while True:
        gallona = float(input("Anna bensiinimäärä gallonoina (negatiivinen lopettaa): "))
        if gallona < 0:
            print("Ohjelma lopetetaan.")
            break
        litraa = gallona_litroiksi(gallona)
        print(f"{gallona} gallonaa on {litraa:.3f} litraa.")


if __name__ == "__main__":
    main()