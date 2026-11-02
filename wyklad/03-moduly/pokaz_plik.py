import sys


def wyswietl_plik(nazwa):
    with open(nazwa, encoding="utf-8") as plik:
        print(plik.read(), end="")


def main():
    if len(sys.argv) > 1:
        nazwa = sys.argv[1]
    else:
        nazwa = input("Nazwa pliku: ")
    wyswietl_plik(nazwa)


if __name__ == "__main__":
    main()
