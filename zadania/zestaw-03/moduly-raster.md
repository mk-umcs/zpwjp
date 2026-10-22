# Moduły, programowanie obiektowe

## Zadanie 1. Operacje na danych rastrowych

Zadanie polega na zaimplementowaniu zestawu narzędzi do operowania na danych rastrowych:
- modułu funkcji do operacji na listach dwuwymiarowych,
- klasy `Raster`,
- programu do operacji na rastrach.

---

### Zadanie 1.1. Podstawowy moduł narzędziowy

Stwórz moduł (np. `narzedzia_rastrowe.py`) funkcji operujących na dwuwymiarowych listach reprezentujących dane rastrowe. Funkcje te **nie mogą** używać operacji wejścia-wyjścia (np. nie mogą same pobierać danych funkcją `input` ani ich drukować za pomocą `print`). Wyjątkiem są te funkcjie, których zadaniem jest właśnie operacja wejścia-wyjścia i jest to wprost powiedziane w opisie.

Zaimplementuj następujące funkcje:

1. **`wczytaj_raster()`** – Pyta użytkownika o liczbę wierszy i kolumn, a następnie w pętli pobiera wartości kolejnych komórek. Funkcja zwracaja dwuwymiarową listę liczb zmiennoprzecinkowych. Każdy wiersz jest pojedynczą listą.
2. **`raster_na_napis(raster)`** – Przyjmuje dwuwymiarową listę i zwraca jej tekstową reprezentację. Kolejne wiersze powinny być oddzielone znakiem nowej linii (`\n`), a poszczególne elementy w wierszu spacją, np. `"1.5 3.4\n-2.0 8.1"`.
3. **`poprawny(raster)`** – Predykat (funkcja zwracająca wartość `True` lub `False`). Sprawdza, czy przekazana lista ma poprawny kształt rastra:
    * liczba wierszy musi być większa od 0,
    * długość każdego wiersza (liczba kolumn) musi być taka sama i większa od 0.

4. **`min_maks(macierz)`** – Zwracaja krotkę z dwiema wartościami: najmniejszą i największą wartością występującą w rastrze.
5. **`srednia(macierz)`** – Zwraca średnią arytmetyczną wszystkich elementów rastra.

**Program główny (podstawowy test modułu):**

Napisz prosty program testujący możliwości modułu. Program używając funkcji modułu po kolei:
- pobiera raster od użytkownika,
- wyświetla raster,
- wyświetla statystyki rastra.

Program testujący ma się uruchamiać tylko jeżeli plik zostanie uruchomiony bezpośrednio, a nie jeżeli zaimportowany.
* Wskazówka: sprawdź wartość zmiennej `__name__`.

---

### Zadanie 1.2. Klasa `Raster`

Stwórz plik `raster.py` zawierający definicję klasy `Raster`, która będzie organizowała pracę z napisanymi wcześniej funkcjami w sposób obiektowy. Klasa powinna używać funkcji z modułu `narzedzia_rastrowe` do wykonania operacji wszędzie tam gdzie jest to możliwe i ma sens.

**Pola klasy:**

Obiekt klasy `Raster` po utworzeniu powinien posiadać trzy pola:
* `tablica` – przechowująca dwuwymiarową listę z wartościami.
* `wysokosc` – liczba wierszy.
* `szerokosc` – liczba kolumn.

**Zaimplementuj następujące metody:**

1. Konstruktor 
    ```python
    __init__(self, raster)
    ```
    * Otrzymuje dwuwymiarową listę.
    * Używa funkcji `poprawny` do sprawdzenia kształtu rastra. Zgłasza wyjątek `ValueError` jeżeli kształt jest zły.
    * Obiekt ma utworzyć swoją kopię danych przekazanych jako argument tak, żeby zapobiec ich przypadkowej modyfikacji z np. z powodu późniejszej modyfikacji tych danych. Możesz użyć funkcji `deepcopy` z modułu `copy`.
    * Ustawia odpowiednio wartości pól `wysokosc` i `szerokosc` na podstawie wymiarów przekazanej listy.


2. Konwersja na napis (`__str__`)

    Zwraca napis sformatowany tak jak robi to funkcja `raster_na_napis` (uży jej do implementacji metody).

3. Konwersja na tekstową reprezentację obiektu (`__repr__`)

    Zwraca standardową tekstową reprezentację obiektu, przydatną dla programisty. Zwracany napis powinien mieć postać zbliżoną do wywołania konstruktora, np. `Raster([[1.0, 2.0], [3.0, 4.0]])`.

4. Metody statystyczne

    Napisz trzy osobne metody do obliczania prostych statystyk:
    * `min()`,
    * `maks()`,
    * `srednia()`.

    Metody nie przyjmują żadnych argumentów. Każda z metod powinna użyć odpowiedniej funkcji z modułu.

**Program główny (podstawowy test klasy):**

Program testujący klasę powinien robić dokładnie to samo co program testujący moduł, ale używając napisanej klasy (tam gdzie to możliwe).

### Zadanie 1.3. Różne rozszerzenia modułu i klasy

Rozwiń moduł o nowe funkcje, a następnie rozbuduj klasę o metody z nich korzystające.

#### Funkcje modułu

Poniższe funkcje modułu operują na rastrach jako listach dwuwymiarowych.

1. **Wczytywanie danych z pliku**

    Funkcja wczytuje dane rastrowych z pliku tekstowego w formacie CSV i zwraca je jako listę. Funkcja powinna obsługiwać sytuacje błędne:
    - W przypadku braku pliku: zgłasza wyjątek `FileNotFoundError`
    - W przypadku błędów w danych: zgłasza wyjątek `ValueError`

    Przykładowy plik z danymi (CSV z przecinkami jako separatorami) może wyglądać tak:
    ```
    195.4,195.4,198.4,200.1,200.2,200.8
    195.3,195.4,181.0,195.2,181.3,300.3
    189.2,198.4,200.5,200.5,190.3,198.2
    ```    

2. **Zapis rastra do pliku**

    Funkcja zapisuje dane rastrowe do pliku tekstowego w formacie CSV.

3. **Wartość najczęstsza (moda)**
    
    Funkcja wyznacza wartość najczęściej występującą. Takich wartości może być wiele, więc funkcja może albo zwracać dowolną z nich, albo zawsze zwracać listę najczęściej występujących wartości.

4. **Zmniejszenie rastra**

    Funkcja zmniejszaja rozmiar rastra o podaną liczbę komórek z każdej strony. Funkcja nie modyfikuje otrzymanego rastra, zwraca nowy o zmniejszonym rozmiarze.

5. **Kompresja rastra**

    Funkcja zmniejsza rozdzielczość rastra przez wyznaczenie nowej wartości komórki jako średniej z sąsiednich pól. Funkcja otrzymuje parametr określający rozmiar okna do kompresji (np. 2 oznacza okno 2×2, 3 oznacza okno 3×3). W przypadku, gdy liczba kolumn lub wierszy nie jest podzielna przez zadany rozmiar okna, pozostałe komórki są pomijane (obcinane). Funkcja nie modyfikuje otrzymanego rastra, zwraca nowy o zmniejszonym rozmiarze.

6. **Operacje z maską**

    Funkcje obliczające minimum, maksimum, średnią i modę ale z dodatkowym parametrem &mdash; maską. Maska jest rastrem z wartościami logicznymi (lub liczbowymi interpretowanymi w sposób logiczny: 0  &mdash; `False`, w przeciwnym razie `True`). Funkcje uwzględniają wyłącznie komórki wskazane w masce (te, które mają wartość logiczną `True`). W przypadku maski &bdquo;pustej&rdquo; (same wartości `False`, co oznacza brak danych do obliczeń) funkcja zgłasza wyjątek `ValueError`.


#### Metody klasy `Raster`

Dopisz dodatkowe metody do klasy `Raster`:
1. metoda `dane()` zwracająca kopię danych rastra &mdash; listę list,
2. metoda obliczająca modę,
3. metoda zmniejszająca raster,
4. metoda kompresująca raster,
5. metody do operacji z maską z dodatkowym parametrem &mdash; maską.

**Uwaga:** Metody w klasie mają nie modyfikować obiektu (pól `tablica`, `wysokosc` i `szerokosc`), na którym zostały wywołane. W razie potrzeby metoda powinna zwrócić nowy obiekt klasy `Raster`.

### Zadanie 1.4. Program główny

Napisz program używający napisanej klasy i modułu.

1. Jeżeli program został uruchomiony z parametrem wiersza poleceń , potraktuj pierwszy argument jako ścieżkę do pliku tekstowego i z niego wczytaj raster.

    W przypadku błędu odczytu (wyjątki zgłoszone z modułu/klasy) program powinien wypisać sensowny komunikat i się zakończyć.

2. Jeżeli programu użyto bez argumentów, wymuś ręczne wczytanie rastra od użytkownika.

3. Utwórz z wczytanych danych obiekt `Raster`.

4. Wyświetl w pętli menu tekstowe pozwalające użytkownikowi na wielokrotne wybieranie i wykonywanie przygotowanych operacji (wyświetlenie statystyk, wyświetlenie danych, zapisanie, itp.).


