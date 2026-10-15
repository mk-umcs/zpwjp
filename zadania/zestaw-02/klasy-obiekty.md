# Zadania: Klasy i obiekty

## 1. Trójkąty

Napisz klasę `Trojkat`. Konstruktor klasy ma dwa parametry: wysokość i podstawę trójkąta (w tych samych jednostkach długości). Wartości tych parametrów są po skonstruowaniu przechowywane w odpowiednich polach. Klasa ma oprócz konstruktora metodę:

- `pole` — zwraca pole powierzchni trójkąta.

**Funkcje**

Napisz następujące funkcje:

- `najwieksze_pole` — dla sekwencji (np. listy, krotki) obiektów typu `Trojkat` zwraca powierzchnię największego trójkąta,
- `trojkaty_w_zakresie_pola` — dla sekwencji (np. listy lub krotki) obiektów typu `Trojkat` oraz dwóch liczb (dolnej i górnej granicy zakresu) zwraca listę trójkątów, których pole mieści się w podanym zakresie.

**Program**

Napisz program testujący klasę i powyższe funkcje. Program powinien pobierać liczbę trójkątów oraz ich parametry od użytkownika i tworzyć ich listę. 
Następnie program ma wyświetlić pole największego z tych trójkątów. W kolejnym kroku program pobiera od użytkownika zakres pól i wyświetla wysokość oraz długość podstawy tych trójkątów, których pola znajdują się w podanym zakresie.

## 2. Miasta

**Klasa `Miasto`**

Napisz klasę `Miasto`. Konstruktor klasy ma trzy parametry: nazwę, powierzchnię w km² oraz populację. Wartości tych parametrów są po skonstruowaniu przechowywane w odpowiednich polach. Klasa ma oprócz konstruktora dwie metody:

- `gestosc_zaludnienia` — zwraca gęstość zaludnienia miasta w osobach na km²,
- `duze` — zwraca informację o tym, czy miasto jest duże (tzn. jego populacja wynosi co najmniej 100 tys. osób).

**Funkcje**

Napisz następujące funkcje:

- `najwieksza_powierzchnia` — dla sekwencji (np. listy, krotki) obiektów typu `Miasto` zwraca powierzchnię największego miasta,
- `najwieksza_gestosc` — dla sekwencji obiektów typu `Miasto` zwraca gęstość najgęściej zaludnionego miasta,
- `nazwy_duzych_miast` — dla sekwencji obiektów typu `Miasto` zwraca listę nazw dużych miast.

**Program**

W pliku tekstowym przechowywana jest informacja o miastach. W każdym wierszu są oddzielone przecinkami kolejno: nazwa, powierzchnia w kilometrach kwadratowych i populacja. Przykładowy plik wejściowy:

```{literalinclude} zestaw-02/miasta.txt
```

Napisz program, który dla takiego pliku wyświetli:

* powierzchnię największego miasta,

* gęstość zaludnienia najgęściej zaludnionego miasta,

* nazwy wszystkich miast, których populacja wynosi co najmniej 100 tysięcy osób.



Dla powyższego pliku wyjście powinno wyglądać następująco:

```text
największa powierzchnia: 2190.93 km²
największa gęstość zaludnienia: 6363.898435824057 os./km²
duże miasta: Lublin, Warszawa, Tokio

```

Program powinien używać klasy `Miasto` oraz napisanych wcześniej funkcji `najwieksza_powierzchnia`, `najwieksza_gestosc` i `nazwy_duzych_miast`.
