"""Klasy wspólne dla programów pracujących z trasami."""

import copy


class Wspolrzedne:
    """Współrzędne punktu: długość i szerokość geograficzna."""

    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def __repr__(self):
        return (
            f"Wspolrzedne({self.dlugosc!r}, {self.szerokosc!r})"
        )


class Trasa:
    """Nazwana trasa złożona z kolejnych punktów."""

    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.przebieg = []

    def dodaj_punkt(self, punkt):
        """Dodaj punkt na końcu trasy."""
        self.przebieg.append(punkt)

    def __repr__(self):
        return (
            f"<Trasa nazwa={self.nazwa!r}, "
            f"przebieg={self.przebieg!r}>"
        )


class Uzytkownik:
    """Użytkownik z listą ulubionych tras."""

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ulubione_trasy = []

    def dodaj_ulubiona(self, trasa):
        """Dodaje ulubioną trasę."""
        self.ulubione_trasy.append(trasa)

    def __repr__(self):
        return (
            f"<Uzytkownik imie={self.imie!r}, "
            f"nazwisko={self.nazwisko!r}, "
            f"ulubione_trasy={self.ulubione_trasy!r}>"
        )

    def kopiuj_ulubione(self, inny):
        """Kopiuje ulubione trasy innego użytkownika."""
        self.ulubione_trasy.extend(
            copy.deepcopy(inny.ulubione_trasy)
        )


def main():
    punkt1 = Wspolrzedne(22.5, 51.2)
    punkt2 = Wspolrzedne(22.6, 51.3)
    trasa = Trasa("Spacer")
    trasa.dodaj_punkt(punkt1)
    trasa.dodaj_punkt(punkt2)
    jan = Uzytkownik("Jan", "Kowalski")
    jan.dodaj_ulubiona(trasa)
    print(jan)


main()
