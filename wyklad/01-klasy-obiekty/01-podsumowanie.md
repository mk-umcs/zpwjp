# Programowanie obiektowe &mdash; Klasy i obiekty &mdash; podsumowanie

## Terminologia (trzeba znać i rozumieć te terminy):
- klasa
- obiekt/egzemplarz klasy
- pole
- metoda
- składowa
- konstruktor
- metoda specjalna

## Umiejętności i wiedza:
- napisanie prostej klasy z polami, konstruktorem i metodami
- utworzenie obiektu (egzemplarza klasy)
- używanie obiektu (i składowych obiektu)
    - używanie pól
    - używanie metod
- tworzenie i używanie metod specjalnych `__repr__` i `__str__`
    - różnica między `__repr__` a `__str__`

## Ćwiczenia sprawdzające

Celem ćwiczeń jest samodzielne sprawdzenie zrozumienia materiału z wykładu i umiejętności użycia go. Jeżeli potrafisz je wykonać, powinieneś być przygotowany do wykorzystania wiedzy z wykładu na laboratorium.

Jeżeli czegoś nie rozumiesz lub nie potrafisz wykonać, wróć do odpowiedniego fragmentu wykładu i spróbuj ponownie.

Część ćwiczeń zakłada wykonanie ich w trybie interaktywnym z załadowanymi odpowiednimi plikami źródłowymi. Możesz zamiast tego dopisać kod źródłowy wykonujący odpowiednie czynności i wyświetlający istotne informacje.

* [Przykładowe odpowiedzi do ćwiczeń](odpowiedzi)

### 1. Utworzenie klasy

Utwórz klasę `Wspolrzedne`.

Klasa ma reprezentować parę współrzędnych zapisanych jako dwie liczby zmiennoprzecinkowe:

- `dlugosc` — długość geograficzna,
- `szerokosc` — szerokość geograficzna.

Klasa powinna mieć konstruktor przyjmujący obie wartości i zapisujący je w odpowiednich polach obiektu.

### 2. Utworzenie obiektu

Uruchom interpreter Pythona w trybie interaktywnym.

- Utwórz obiekt klasy `Wspolrzedne` reprezentujący punkt o współrzędnych:

    - długość: `22.57`,
    - szerokość: `51.25`.

- Przypisz obiekt do zmiennej `lublin`.

- Sprawdź wartości obu pól obiektu.

### 3. Zmiana wartości pól

- Zmień wartość pola `dlugosc` obiektu `punkt` na wybraną wartość.

- Sprawdź wartość tego pola.

- Podstaw z powrotem pod pole jego poprzednią wartość.

- Zrób to samo dla pola `szerokosc`.

### 4. Używanie pól

- Utwórz drugi obiekt klasy `Wspolrzedne` reprezentujący punkt o współrzędnych:

    - długość: `21.01`,
    - szerokość: `52.23`.

    Przypisz obiekt do zmiennej `warszawa`.

- Użyj wartości pól obiektów do skonstruowania prostych wyrażeń logicznych i arytmetycznych, np.

    - oblicz różnicę długości geograficznych punktów,
    - sprawdź, czy pierwszy punkt jest położony na południe od drugiego (ma mniejszą szerokość).

### 5. Tworzenie metod

Dopisz do klasy metodę `polkula_polnocna`, która:

- nie przyjmuje żadnych argumentów (oprócz `self`),
- zwraca `True`, jeśli szerokość geograficzna jest większa od zera, a w przeciwnym razie `False`.

**Uwagi:**
- Wynik ma być **zwracany** przez metodę (`return`). Metoda ma niczego nie wyświetlać.
- Pamiętaj o załadowaniu poprawionej definicji klasy przed wykonaniem kolejnych ćwiczeń w sesji interaktywnej.

### 6. Używanie metod

- Utwórz przykładowe obiekty typu `Wspolrzedne` w tym reprezentujące punkty leżące na półkuli północnej, na półkuli południowej i na równiku.
- Wypróbuj na nich działanie metody.
- Zmień kilka razy wartość pola `szerokosc` w jednym z obiektów. Użyj zarówno wartości ujemnych, dodatnich oraz zera. Po każdej zmianie sprawdź działanie metody dla tego punktu.
- Napisz i wypróbuj funkcję, która dostaje jeden argument typu `Wspolrzedne` i używając metody `polkula_polnocna` wyświetla informację o tym, czy punkt leży na półkuli północnej.

### 7. Metody `__repr__` i `__str__`

- Na wybranym obiekcie typu `Wspolrzedne` wypróbuj w trybie interaktywnym:
    - wpisanie samej nazwy zmiennej:
        ```python-repl
        >>> lublin
        ```
    - wywołanie `repr`:
        ```python-repl
        >>> repr(lublin)
        ```
    - wywołanie `str`:
        ```python-repl
        >>> str(lublin)
        ```
    - wywołanie `print`:
        ```python-repl
        >>> print(lublin)
        ```
    - użycie f-stringów:
        ```python-repl
        >>> f"{lublin}"
        ```
    - użycie f-stringów z flagą `!r`:
        ```python-repl
        >>> f"{lublin!r}"
        ```

- Dodaj do klasy metodę specjalną `__repr__` zwracającą napis w postaci
    ```python
    "Wspolrzedne(22.57, 51.25)"
    ```
    i wykonaj to samo ponownie.

- Dodaj do klasy metodę specjalną `__str__` zwracającą napis w postaci
    ```python
    "(22.57°, 51.25°)"
    ```
    i wykonaj jeszcze raz to samo.
    
    Symbol stopnia możesz uzskać np. za pomocą sekwencji `\u00b0`, np. `print("(22\u00b0, 51\u00b0)")` wyświetli napis `(22°, 51°)`.
