# Klasy, współpraca obiektów i kopie: łamane

1. Napisz klasę `Lamana` reprezentujacą [linię łamaną](https://pl.wikipedia.org/wiki/Linia_%C5%82amana). Nowo utworzona łamana jest pusta (nie zawiera żadnych punktów). Do łamanej możemy dodawać kolejne punkty (metodą `dodaj_punkt`). Napisz metodę `dodaj_punkt`, metodę `dlugosc` zwracającą długość łamanej oraz metodę `__str__` zwracającą napisową reprezentację łamanej w formacie [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry). 

    Punkt może być reprezentowany jako

    ```python
     class Punkt:

        def __init__(self, x, y):
            self.x = x
            self.y = y
    ```


    Przykład:

    ```pycon
    >>> lamana = Lamana()
    >>> print(lamana)
    LINESTRING EMPTY
    >>> lamana.dodaj_punkt(Punkt(0, 0))
    >>> print(lamana)
    LINESTRING (0 0)
    >>> lamana.dodaj_punkt(Punkt(3, 4))
    >>> lamana.dodaj_punkt(Punkt(0, 4))
    >>> lamana.dodaj_punkt(Punkt(0, 2))
    >>> print(lamana)
    LINESTRING (0 0, 3 4, 0 4, 0 2)
    >>> lamana.dlugosc()
    10
    ```

1. Plik w formacie [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) możemy w łatwy sposób przeczytać i załadować do słownika używając funkcji `load` z modułu [`json`](https://docs.python.org/3/library/json.html) w następujący sposób:

        >>> import json
        >>> plik = open('lamana.json')
        >>> lamana_json = json.load(plik)
        >>> lamana_json
        {'type': 'LineString', 'coordinates': [[30, 10], [10, 30], [40, 40]]}
        >>> lamana_json['coordinates']
        [[30, 10], [10, 30], [40, 40]]

    Napisz program korzystający z klasy `Lamana` umożliwiający konwersję pliku przechowującego łamaną w formacie GeoJSON (`LineString`) na plik w formacie WKT. Nazwy pliku wejściowego (GeoJSON) i wynikowego (WKT) pobierane są od użytkownika.

    Plik [lamana.json](pliki/lamana.json).

1. Klasa `Lamana` z poprzednich zadań może przechowywać punkty w liście w następujący sposób:

    ```python
    class Punkt:

        def __init__(self, x, y):
            self.x = x
            self.y = y


    class Lamana:

        def __init__(self):
            self.punkty = []

        def dodaj_punkt(self, punkt):
            self.punkty.append(Punkt(punkt.x, punkt.y))
    ```


    Napisz klasę `ZbiorLamanych` reprezentującą zbiór łamanych (MultiLineString). Nowo utworzony zbiór nie zawiera żadnych łamanych. Do zbioru możemy dodawać kolejne łamane za pomocą metody `dodaj_lamana`. Łamane mogą być przechowywane w liście — w polu `lamane`. Napisz metodę `dodaj_lamana` tak, żeby obiekt typu `ZbiorLamanych` przechowywał w liście kopie łamanych przekazywanych w argumentach, a nie referencje do zadanych obiektów (punkty, z których składają się łamane również mają być skopiowane) — ewentualne późniejsze zmiany w obiektach przekazanych jako argument `dodaj_lamana` i ich składowych nie powinny mieć wpływu na obiekt zbioru.

    ```pycon
    >>> zbior = ZbiorLamanych()
    >>> lamana1 = Lamana()
    >>> lamana1.dodaj_punkt(Punkt(3, 4))
    >>> lamana1.dodaj_punkt(Punkt(10, 20))
    >>> zbior.dodaj_lamana(lamana1)
    >>> lamana2 = Lamana()
    >>> lamana2.dodaj_punkt(Punkt(-4, -5))
    >>> lamana2.dodaj_punkt(Punkt(8, 7))
    >>> zbior.dodaj_lamana(lamana2)
    ```

    Modyfikujemy punkty w pierwszej łamanej i samą łamaną:

    ```pycon
    >>> lamana1.punkty[0].x = 777
    >>> lamana1.dodaj_punkt(Punkt(7, 7))
    ```

    Zbiór łamanych pozostaje bez zmian:

    ```pycon    
    >>> len(zbior.lamane[0].punkty)
    2
    >>> zbior.lamane[0].punkty[0].x
    3
    ```

## Uzupełnienie: zapis zbioru łamanych

Dodaj do klasy `ZbiorLamanych` metodę `__str__` zwracającą zapis WKT, analogicznie do metody klasy `Lamana`. Użyj typu `MULTILINESTRING`, a dla pustego zbioru — `MULTILINESTRING EMPTY`.

Napisz program konwertujący geometrię GeoJSON `MultiLineString` na WKT z użyciem tej klasy. Zachowaj wszystkie łamane i kolejność ich punktów.
