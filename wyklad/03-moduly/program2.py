import copy
import trasy


def main():
    trasa = trasy.Trasa("Spacer")
    trasa.dodaj_punkt(trasy.Wspolrzedne(22.5, 51.2))
    trasa.dodaj_punkt(trasy.Wspolrzedne(22.6, 51.3))
    kopia = copy.deepcopy(trasa)
    kopia.nazwa = "Dłuższy spacer"
    kopia.przebieg[1].szerokosc = 51.4
    print(trasa)
    print(kopia)


if __name__ == "__main__":
    main()
