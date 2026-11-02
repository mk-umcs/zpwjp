import copy
import trasy_program


def main():
    trasa = trasy_program.Trasa("Spacer")
    trasa.dodaj_punkt(trasy_program.Wspolrzedne(22.5, 51.2))
    trasa.dodaj_punkt(trasy_program.Wspolrzedne(22.6, 51.3))
    kopia = copy.deepcopy(trasa)
    kopia.nazwa = "Dłuższy spacer"
    kopia.przebieg[1].szerokosc = 51.4
    print(trasa)
    print(kopia)


if __name__ == "__main__":
    main()
