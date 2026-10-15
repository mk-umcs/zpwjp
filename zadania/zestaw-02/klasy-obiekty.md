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


## 3. Punkty i Koła

**Klasa `Punkt`**

Napisz klasę `Punkt`, która reprezentuje punkt w przestrzeni dwuwymiarowej z metodami umożliwiającymi zmianę położenia i obliczenie odległości między dwoma punktami.

Klasa ma mieć następujące metody:
* konstruktor dwuargumentowy przyjmujący współrzędne: `x`, `y`,
* metoda `przesun(dx, dy)` — przesuwa punkt o wektor zadany współrzędnymi `dx` i `dy`,
* metoda `odleglosc(drugi_punkt)` — zwraca odległość euklidesową do innego punktu (drugi punkt podany jako argument),
* metoda `czy_rowny(drugi_punkt)` — zwraca `True`, jeśli punkty mają takie same współrzędne,
* odpowiednia metoda `__repr__`.

**Klasa `Kolo`**

Napisz klasę `Kolo`, która reprezentuje koło o zadanym środku (obiekcie klasy `Punkt`) i promieniu.

Klasa ma mieć następujące metody:
* konstruktor dwuargumentowy, który umożliwia wywołanie: `Kolo(punkt_srodka, promien)`,
* metoda `przesun(dx, dy)` — przesuwa koło (pamiętaj, klasę zaimplementować tak, by podczas przesuwania koła sam przekazany pierwotnie do konstruktora obiekt punktu zachował swoje oryginalne współrzędne),
* metoda `czy_rowne(drugie_kolo)` — zwraca `True`, jeśli koła mają identyczne środki i promienie,
* metoda `zawiera(punkt)` — sprawdza, czy dany obiekt klasy `Punkt` należy do koła (znajduje się w jego wnętrzu lub na brzegu),
* odpowiednia metoda `__repr__`.

**Funkcja filtrująca punkty w kole**

Napisz funkcję `punkty_w_kole(kolo, sekwencja_punktow)`, która zwraca listę tych punktów z przekazanej sekwencji, które należą do przekazanego koła.

## 4. Miasta w pobliżu innych miast

W tym zadaniu przyjmujemy, że współrzędne `x`, `y` oznaczają współrzędne w układzie **EPSG:2180** (**w metrach**).

Mamy plik tekstowy zawierający miasta w formacie `nazwa miasta;x;y`.

Przykładowy plik (`miasta_wspolrzedne.txt`):

```{literalinclude} zestaw-02/miasta_wspolrzedne.txt
```

*Wskazówka:* Plik do testów z wszystkimi miastami polskimi (stan na 2025 rok) znajdziesz w pliku [miasta_wspolrzedne_2025.txt](zestaw-02/miasta_wspolrzedne_2025.txt).

Napisz program, który:
1. wczytuje plik z miastami,
2. pyta użytkownika o nazwę miasta,
3. pyta o odległość w kilometrach,
4. znajduje wszystkie miasta nie dalsze niż zadana odległość od wybranego miasta,
5. wypisuje znalezione miasta wraz z obliczoną odległością.

Użyj klasy `Kolo` do reprezentowania odpowiedniego bufora wokół wybranego miasta i stworzonej wcześniej metody `zawiera` do sprawdzenia, czy dane miasto leży w tym buforze.

## 5. System zarządzania pracownikami i umiejętnościami

Zdefiniuj trzy klasy, które posłużą do gromadzenia informacji o pracownikach oraz ich kompetencjach. Pierwsze dwie z nich są klasami wyłącznie do grupowania danych.

**Klasa `PelneNazwisko`**
Klasa przechowująca dane osobowe. Klasa ma wyłącznie następujące składowe:
* konstruktor,
* pola: `imie`, `nazwisko`,
* metody specjalne: `__str__` oraz `__repr__`.

**Klasa `Umiejetnosc`**
Klasa przechowująca dane o konkretnej kompetencji.
* posiada wyłącznie konstruktor,
* pola: `nazwa`, `poziom` (np. liczba całkowita określająca poziom zaawansowania),
* metody specjalne `__str__` oraz `__repr__`.

**Klasa `Pracownik`**
Klasa reprezentująca pojedynczego pracownika w systemie.

* podczas tworzenia przyjmuje tylko pełne nazwisko (obiekt klasy `PelneNazwisko`),
* nowy pracownik zostaje automatycznie stworzony z pustą strukturą umiejętności,
* posiada następujące metody do zarządzania kompetencjami:
* `ustaw_poziom_umiejetnosci(nazwa, poziom)` — jeżeli pracownik nie ma jeszcze podanej umiejętności, dodaje ją z określonym poziomem, w przeciwnym razie zmienia jej obecny poziom,
* `usun_umiejetnosc(nazwa)` — usuwa daną umiejętność z profilu pracownika,
* `ma_umiejetnosc(nazwa)` — sprawdza, czy pracownik posiada konkretną umiejętność,
* `poziom_umiejetnosci(nazwa)` — zwraca przypisany poziom dla danej nazwy, wyrzuca wyjątek `ValueError`, jeżeli takiej umiejętności w ogóle nie ma w profilu pracownika,
* `umiejetnosci_na_poziomie(poziom)` — zwraca listę nazw tych umiejętności pracownika, których poziom jest większy lub równy podanemu argumentowi.
* `ma_umiejetnosc_na_poziomie(nazwa, poziom)` — weryfikuje, czy pracownik posiada wybraną umiejętność, a jej poziom jest co najmniej taki, jak oczekiwany.


*Wskazówka:* Przy pisaniu klasy `Pracownik` rozważ dwie różne implementacje do przechowywania kompetencji i samodzielnie wybierz optymalniejszą:

1. opartą o klasyczną listę obiektów klasy `Umiejetnosc`,
2. opartą o słownik realizujący mapowanie typu `nazwa_umiejetnosci -> poziom`.

## 6. Przetwarzanie danych pracowników (pliki tekstowe)

Przygotuj programy przetwarzające pliki tekstowe z danymi pracowników w odpowiednim formacie.

**Program 1**

W pliku pierwsza linijka to zawsze imię i nazwisko osoby. Każdy kolejny wiersz określa posiadaną kompetencję w formacie `umiejętność: poziom`.

Napisz program, który odczytuje takie dane, pyta użytkownika o wymagany poziom, a następnie wyświetla wszystkie umiejętności pracownika równe lub wyższe wskazanemu progowi. *Wymóg:* Musisz użyć stworzonej przed chwilą instancji klasy `Pracownik` i wykorzystać jej metody logiczne do tego filtra.

**Program 2**

Zasada zapisu jest podobna, ale tym razem w pliku figuruje wielu pracowników naraz. Pojedynczy pusty wiersz oddziela wpisy poszczególnych osób.

1. Napisz dodatkową funkcję globalną, która przyjmuje listę obiektów klas `Pracownik` i wyciąga z nich listę samych pełnych nazwisk w postaci napisów.
2. Stwórz program, który pyta o docelową umiejętność oraz minimalny poziom jej znajomości, a następnie (wykorzystując metodę `ma_umiejetnosc_na_poziomie` i swoją nową funkcję) zwraca same pełne nazwiska kwalifikujących się do zadania osób.
