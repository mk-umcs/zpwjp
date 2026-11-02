# Referencje i kopie obiektów — podsumowanie

## Terminologia (trzeba znać i rozumieć te terminy)

- referencja,
- płytka kopia (ang. *shallow copy*),
- głęboka kopia (ang. *deep copy*).

## Umiejętności i wiedza

- odróżnianie przypisania od utworzenia kopii obiektu,
- rozpoznanie, kiedy dwie referencje wskazują na ten sam obiekt,
- odróżnianie zmiany wartości pola (zmiany referencji) od modyfikacji obiektu wskazywanego przez to pole,
- tworzenie płytkich i głębokich kopii np. za pomocą funkcji [`copy.copy`](https://docs.python.org/3/library/copy.html#copy.copy) i [`copy.deepcopy`](https://docs.python.org/3/library/copy.html#copy.deepcopy),

## Ćwiczenia sprawdzające

Celem ćwiczeń jest samodzielne sprawdzenie zrozumienia materiału z wykładu i umiejętności użycia go. Jeżeli potrafisz je wykonać, masz podstawy do wykorzystania wiedzy z wykładu na laboratorium.

Jeżeli czegoś nie rozumiesz lub nie potrafisz wykonać, wróć do odpowiedniego fragmentu wykładu i spróbuj ponownie.

Część ćwiczeń zakłada wykonanie ich w trybie interaktywnym z załadowanymi odpowiednimi plikami źródłowymi. Możesz zamiast tego dopisać kod źródłowy wykonujący odpowiednie czynności i wyświetlający istotne informacje.

* [Przykładowe odpowiedzi do ćwiczeń](odpowiedzi-1)

### Wprowadzenie

Dwa czujniki mogą być zamontowane w tym samym miejscu. Ich położenie opisuje obiekt ze współrzędnymi `x`, `y`, `z`. Skorzystaj z poniższych definicji. Konstruktor `Czujnik` w tej wersji **nie kopiuje** położenia. W każdym ćwiczeniu utwórz obiekty od nowa, zgodnie z podanym początkiem.

```python
class Polozenie:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Polozenie({self.x!r}, {self.y!r}, {self.z!r})"


class Czujnik:
    def __init__(self, nazwa, model, polozenie):
        self.nazwa = nazwa
        self.model = model
        self.polozenie = polozenie
```

### 1. Dwie zmienne, jeden obiekt

- Utwórz zmienne `pozycja1` i `pozycja2` w następujący sposób:
    ```python
    pozycja1 = Polozenie(10, 20, 30)
    pozycja2 = pozycja1
    ```
- Jaki będzie wynik sprawdzenia `pozycja1 is pozycja2`?
- Zmień wartość `pozycja2.z` na `35`. Jaka będzie wartość `pozycja1.z`?

(wspolne-pola)=
### 2. Wspólne pole dwóch obiektów

- Utwórz zmienną `pozycja` z wartością `Polozenie(10, 20, 30)` oraz czujniki `pierwszy` i `drugi`, używając w obu przypadkach pozycji ze zmiennej `pozycja`.
- Jakie będą wyniki sprawdzenia `pierwszy is drugi` oraz `pierwszy.polozenie is drugi.polozenie`?
- Zmień wartość `drugi.polozenie.z` na `35`. Sprawdź czy zmieniło się położenie pierwszego czujnika i obiekt `pozycja`?

### 3. Płytka kopia

- Utwórz od nowa czujnik `pierwszy` z wartością `Czujnik("T1", "A", Polozenie(10, 20, 30))`.
- W zmiennej `kopia` utwórz jego płytką kopię używając odpowiedniej funkcji z modułu `copy`.
- Jakie będą wyniki sprawdzenia `kopia is pierwszy` oraz `kopia.polozenie is pierwszy.polozenie`.
- Wykonaj podstawienia:
    ```python
    kopia.nazwa = "T3"
    kopia.polozenie.z = 35
    ```
    
    - Czy zmieniła się nazwa pierwszego czujnika?
    - Czy zmieniło się położenie pierwszego czujnika?
    - Dlaczego skutki tych zmian są różne?

### 4. Głęboka kopia

- Powtórz poprzednie ćwiczenie, ale utwórz głęboką kopię obiektu.

### 5. Kopia w konstruktorze

- Zmień w konstruktor klasy `Czujnik` tak, żeby pod pole `polozenie` podstawiał nowy obiekt `Polozenie` z takimi samymi wartościami pól jak obiekt przekazany jako argument.
- Wykonaj ponownie ćwiczenie &bdquo;{ref}`Wspólne pole dwóch obiektów <wspolne-pola>`&rdquo;.

    **Uwaga:** Pamiętaj, żeby załadować nową definicję klasy przed utworzeniem obiektów.