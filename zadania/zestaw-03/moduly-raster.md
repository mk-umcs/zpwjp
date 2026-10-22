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

3. Konwersja na tekstową reprezentację obiektu ()`__repr__`

    Zwraca standardową tekstową reprezentację obiektu, przydatną dla programisty. Zwracany napis powinien mieć postać zbliżoną do wywołania konstruktora, np. `Raster([[1.0, 2.0], [3.0, 4.0]])`.

4. Metody statystyczne

    Napisz trzy osobne metody do obliczania prostych statystyk:
    * `min()`,
    * `maks()`,
    * `srednia()`.

    Metody nie przyjmują żadnych argumentów. Każda z metod powinna użyć odpowiedniej funkcji z modułu.

**Program główny (podstawowy test klasy):**

Program testujący klasę powinien robić dokładnie to samo co program testujący moduł, ale używając napisanej klasy (tam gdzie to możliwe).

---

### Zadanie 1.3. Różne rozszerzenia modułu i klasy

Rozwiń moduł o nowe funkcje, a następnie rozbuduj klasę o metody z nich korzystające.

**Uwaga:** Metody w klasie nie modyfikować obiektu (pól `tablica`, `wysokosc` i `szerokosc`), na którym zostały wywołane. W razie potrzeby metoda powinna zwrócić nowy obiekt klasy `Raster`.

Dodaj w module funkcje realizujące:
1. odczyt i zapis z CSV,
2. obliczenie mody (wartości najczęstszej) &mdash; w przypadku wielu takich wartości funkcja może zwrócić dowolną wybraną, lub zwrócić kompletną listę takich wartości (wybierz sposób),
3. zmniejszenie rastra o zadaną liczbę komórek z każdej strony (obcinanie brzegów),
4. kompresja rastra - zmniejszenie rozdzielczości (np. z okna 2x2 komórek powstaje 1 komórka z wartością średnią). Komórki na niepełnych brzegach są ignorowane. W klasie metoda `kompresuj(self, okno)`, zwracająca nową instancję rastra.
5. **Operacje z maską**. Metody statystyczne przyjmujące dodatkowy obiekt klasy `Raster` (maskę). Do obliczeń brane są pod uwagę tylko te pola z bieżącego rastra, na których odpowiadających pozycjach maska posiada wartość potraktowaną jako `True` (różną od 0).

---

## Część IV: Program główny i argumenty wiersza poleceń

Utwórz oddzielny plik (np. `main.py`), który zaimportuje klasę i/lub funkcje z Twojego modułu.

1. Wykorzystaj moduł `sys` i sprawdź zawartość `sys.argv`.
2. Jeżeli program został uruchomiony z parametrem wiersza poleceń (np. `python main.py dane.csv`), potraktuj pierwszy argument jako ścieżkę do pliku tekstowego i z niego wczytaj raster.
3. Jeżeli programu użyto bez argumentów, wymuś ręczne wczytanie rastra od użytkownika (np. poprzez Twoją funkcję narzędziową).
4. Następnie utwórz z tych danych obiekt `Raster` i wyświetl w pętli menu tekstowe pozwalające użytkownikowi na wielokrotne wybieranie i wykonywanie przygotowanych operacji (wyświetlenie statystyk, wyświetlenie danych, zapisanie, itp.). W przypadku błędu odczytu (wyjątki zgłoszone z modułu/klasy) program powinien wypisać sensowny komunikat i się zakończyć.

---

## Część V: Wyzwanie – stan obiektu i aktualizacja danych

W ramach alternatywnego podejścia do obliczeń statystycznych rozważ wprowadzenie do klasy tzw. "pamięci stanu" (buforowania).

1. Napisz funkcję (w module proceduralnym), która jednorazowo iteruje po danych i zwraca **krotkę z czterema wartościami** (min, max, średnia, moda).
2. Dodaj do klasy `Raster` nowe pole `bufor_statystyk` i zainicjalizuj je w konstruktorze jako `None`.
3. Dodaj w klasie metodę `oblicz_statystyki(self)`, która pod spodem wywoła nową funkcję obliczającą, ale **nic nie zwróci** – zamiast tego zapisze otrzymaną krotkę do pola `bufor_statystyk`.
4. Zmień metody `najmniejsza_wartosc(self)`, `srednia(self)` itd. w taki sposób, aby przestały na bieżąco uruchamiać obliczenia. Zamiast tego mają odczytywać z góry określone indeksy z zapisanej w polu `bufor_statystyk` krotki. Jeśli w momencie odpytania to pole wynosi `None`, metody powinny rzucić wyjątek `ValueError` z informacją ("Statystyki nie zostały jeszcze policzone").

**Problem do zastanowienia:** Jeśli użytkownik po użyciu `oblicz_statystyki()` bezpośrednio zmodyfikuje zawartość pola `tablica` (np. przypisując `moj_raster.tablica[0][0] = 999.0`), metody z Części V zwrócą **nieaktualne, fałszywe wyniki**, dopóki ktoś nie wymusi ponownego przeliczenia. Jak widzisz, jawny dostęp do atrybutów bywa ryzykowny – jak można by temu zapobiec, aby obiekt sam kontrolował zmiany swoich danych? Zastanów się nad tym przed kolejnym wykładem!
