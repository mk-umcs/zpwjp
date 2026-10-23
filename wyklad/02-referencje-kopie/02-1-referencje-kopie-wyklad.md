# Programowanie obiektowe &mdash; referencje i kopie obiektów

Jak działa instrukcja podstawienia w przypadku list?
```python
lista1 = [1, 2, 3]
lista2 = lista1
```
Czy powyższy kod utworzył kopię listy `lista1` w zmiennej `lista2`?

Sprawdźmy to modyfikując element listy `lista2`:
```python
lista2[1] = 7
```
i sprawdzając wartość odpowiedniego elementu listy `lista1`:
```python
lista1[1]
```

Modyfikacja wartości w liście wskazywanej przez `b` jest widoczna również jeżeli do odczytu tej wartości użyjemy zmiennej `a`.

Jest tak dlatego, że zmienna `lista1` nie przechowuje listy a **referencję** (ang. *reference*) do niej. Referencja jest tylko informacją gdzie lista się znajduje. Podstawienie oznacza skopiowanie tej informacji. Po wykonaniu podstawienia zmienne `lista1` i `lista2` wskazują na tę samą listę.

**Sprawdź:**
* [Wizualizacja działania referencji do list na stronie Python Tutor](https://pythontutor.com/visualize.html#code=lista1%20%3D%20%5B1,%202,%203%5D%0Alista2%20%3D%20lista1%0Alista2%5B1%5D%20%3D%207%0A%0Aprint%28lista1%5B1%5D%29&curInstr=0&mode=display&origin=opt-frontend.js&py=311)


## Referencje do obiektów

Ten sam mechanizm ma zastosowanie do obiektów. Zmienne nie przechowują obiektów tylko referencje do nich.


```python
class Osoba:
    
    def __init__(self, imie, nazwisko, rok_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok_urodzenia = rok_urodzenia
```

Wypróbujmy podstawienie:
```python
osoba_1 = Osoba("Jan", "Kowalski", 2000)
osoba_2 = osoba_1
```

i zmianę wartości pola:
```python
osoba_2.rok_urodzenia = 2010
```

Teraz sprawdźmy wartość pola za pomocą innej zmiennej niż użyliśmy do zmiany wartości:
```python
osoba_1.rok_urodzenia
```

Mamy teraz tylko jeden obiekt i dwie refrencje do niego.

**Sprawdź:**
* [Wizualizacja działania referencji do obiektów na stronie Python Tutor](https://pythontutor.com/visualize.html#code=class%20Osoba%3A%0A%20%20%20%20def%20__init__%28self,%20imie,%20nazwisko,%20rok_urodzenia%29%3A%0A%20%20%20%20%20%20%20%20self.imie%20%3D%20imie%0A%20%20%20%20%20%20%20%20self.nazwisko%20%3D%20nazwisko%0A%20%20%20%20%20%20%20%20self.rok_urodzenia%20%3D%20rok_urodzenia%0A%20%20%20%20%20%20%20%20%0Aosoba_1%20%3D%20Osoba%28%22Jan%22,%20%22Kowalski%22,%202000%29%0Aosoba_2%20%3D%20osoba_1%0Aosoba_2.rok_urodzenia%20%3D%202010%0A%0Aprint%28osoba_1.rok_urodzenia%29&curInstr=0&mode=display&origin=opt-frontend.js&py=3)



## Referencje jako pola

To samo dotyczy obiektów, które same są polami innych obiektów.

Zdefiniujmy klasę do reprezentowania daty:


```python
class Data:
    def __init__(self, rok, miesiac, dzien):
        self.rok = rok
        self.miesiac = miesiac
        self.dzien = dzien
        
    def __repr__(self):
        return f"Data({self.rok!r}, {self.miesiac!r}, {self.dzien!r})"
```

Następnie poprawmy definicję klasy `Osoba` tak, żeby przechowywała całą datę urodzenia w polu `data_urodzenia` jako obiekt klasy `Data`.


```python
class Osoba:
    def __init__(self, imie, nazwisko, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia

    def __repr__(self):
        return f"Osoba({self.imie!r}, {self.nazwisko!r}, {self.data_urodzenia!r})"
```

Tworzymy obiekt reprezentujący dzień 10 maja 2010 roku:


```python
data = Data(2010, 5, 10)
```

Tworzymy dwa obiekty reprezentujące osoby urodzone tego dnia:

```python
jan = Osoba("Jan", "Kowalski", data)
anna = Osoba("Anna", "Nowak", data)
```

Zmieniamy dzień urodzenia jednej z osób:


```python
anna.data_urodzenia.dzien += 10
```

Sprawdzamy dzień urodzenia drugiej osoby:

```python
jan.data_urodzenia.dzien
```

Widzimy, że data została zmieniona. Spowodowane jest to tym, że osoby dzielą wspólny obiekt `Data`. 

Zmiana widoczna jest też jeżeli użyjemy zmiennej `data`:

```python
data
```


**Sprawdź:**
* [Wizualizacja współdzielenia pól na stronie Python Tutor](https://pythontutor.com/visualize.html#code=class%20Data%3A%0A%0A%20%20%20%20def%20__init__%28self,%20rok,%20miesiac,%20dzien%29%3A%0A%20%20%20%20%20%20%20%20self.rok%20%3D%20rok%0A%20%20%20%20%20%20%20%20self.miesiac%20%3D%20miesiac%0A%20%20%20%20%20%20%20%20self.dzien%20%3D%20dzien%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22Data%28%7Bself.rok!r%7D,%20%7Bself.miesiac!r%7D,%20%7Bself.dzien!r%7D%29%22%0A%20%20%20%20%20%20%20%20%0Aclass%20Osoba%3A%0A%20%20%20%20%0A%20%20%20%20def%20__init__%28self,%20imie,%20nazwisko,%20data_urodzenia%29%3A%0A%20%20%20%20%20%20%20%20self.imie%20%3D%20imie%0A%20%20%20%20%20%20%20%20self.nazwisko%20%3D%20nazwisko%0A%20%20%20%20%20%20%20%20self.data_urodzenia%20%3D%20data_urodzenia%0A%20%20%20%20%20%20%20%20%0A%0Adata%20%3D%20Data%282010,%205,%2010%29%0A%0Ajan%20%3D%20Osoba%28%22Jan%22,%20%22Kowalski%22,%20data%29%0Aanna%20%3D%20Osoba%28%22Anna%22,%20%22Nowak%22,%20data%29%0A%0Aanna.data_urodzenia.dzien%20%2B%3D%2010%0A%0Aprint%28jan.data_urodzenia.dzien%29%0Aprint%28data%29%0A&curInstr=0&mode=display&origin=opt-frontend.js&py=3)


## Kopie obiektów

Jeżeli potrzebujemy kopii obiektu, to możemy ją zrobić tworząc nowy obiekt z identycznymi wartościami pól, np.

```python
data = Data(2010, 5, 10)
kopia_daty = Data(data.rok, data.miesiac, data.dzien)
```

Teraz są to dwa niezależne obiekty:
```python
data.dzien += 10
```
Sprawdźmy:
```python
kopia_daty.dzien
```

**Sprawdź:**
* [Wizualizacja kopii obiektu na stronie Python Tutor](https://pythontutor.com/visualize.html#code=class%20Data%3A%0A%0A%20%20%20%20def%20__init__%28self,%20rok,%20miesiac,%20dzien%29%3A%0A%20%20%20%20%20%20%20%20self.rok%20%3D%20rok%0A%20%20%20%20%20%20%20%20self.miesiac%20%3D%20miesiac%0A%20%20%20%20%20%20%20%20self.dzien%20%3D%20dzien%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22Data%28%7Bself.rok!r%7D,%20%7Bself.miesiac!r%7D,%20%7Bself.dzien!r%7D%29%22%0A%20%20%20%20%0A%0Adata%20%3D%20Data%282010,%205,%2010%29%0Akopia_daty%20%3D%20Data%28data.rok,%20data.miesiac,%20data.dzien%29%0Adata.dzien%20%2B%3D%2010%0A%0Aprint%28kopia_daty.dzien%29%0A&curInstr=0&mode=display&origin=opt-frontend.js&py=3)


Możemy podobnie zrobić w konstruktorze klasy `Osoba` żeby uniknąć takiego powiązania obiektów wspólnymi danymi:


```python
class Osoba:
    
    def __init__(self, imie, nazwisko, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = Data(data_urodzenia.rok, data_urodzenia.miesiac, data_urodzenia.dzien)

    def __repr__(self):
        return f"Osoba({self.imie!r}, {self.nazwisko!r}, {self.data_urodzenia!r})"
```

Sprawdźmy teraz:

```python
data = Data(2010, 5, 10)
jan = Osoba("Jan", "Kowalski", data)
anna = Osoba("Anna", "Nowak", data)

anna.data_urodzenia.miesiac = 2
jan.data_urodzenia.miesiac = 7
```

```python
anna.data_urodzenia
```

```python
jan.data_urodzenia
```

```python
data
```

Widać, że tym razem mamy trzy osobne obiekty typu `Data`.

**Sprawdź:**
* [Wizualizacja tworzenia kopii obiektu w konstruktorze na stronie Python Tutor](https://pythontutor.com/visualize.html#code=class%20Data%3A%0A%0A%20%20%20%20def%20__init__%28self,%20rok,%20miesiac,%20dzien%29%3A%0A%20%20%20%20%20%20%20%20self.rok%20%3D%20rok%0A%20%20%20%20%20%20%20%20self.miesiac%20%3D%20miesiac%0A%20%20%20%20%20%20%20%20self.dzien%20%3D%20dzien%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22Data%28%7Bself.rok!r%7D,%20%7Bself.miesiac!r%7D,%20%7Bself.dzien!r%7D%29%22%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Aclass%20Osoba%3A%0A%20%20%20%20%0A%20%20%20%20def%20__init__%28self,%20imie,%20nazwisko,%20data_urodzenia%29%3A%0A%20%20%20%20%20%20%20%20self.imie%20%3D%20imie%0A%20%20%20%20%20%20%20%20self.nazwisko%20%3D%20nazwisko%0A%20%20%20%20%20%20%20%20self.data_urodzenia%20%3D%20Data%28data_urodzenia.rok,%20data_urodzenia.miesiac,%20data_urodzenia.dzien%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22Osoba%28%7Bself.imie!r%7D,%20%7Bself.nazwisko!r%7D,%20%7Bself.data_urodzenia!r%7D%29%22%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Adata%20%3D%20Data%282010,%205,%2010%29%0Ajan%20%3D%20Osoba%28%22Jan%22,%20%22Kowalski%22,%20data%29%0Aanna%20%3D%20Osoba%28%22Anna%22,%20%22Nowak%22,%20data%29%0A%0Aanna.data_urodzenia.miesiac%20%3D%202%0Ajan.data_urodzenia.miesiac%20%3D%207%0A%0Aprint%28anna.data_urodzenia%29%0Aprint%28jan.data_urodzenia%29%0Aprint%28data%29&curInstr=0&mode=display&origin=opt-frontend.js&py=3).

### Moduł `copy`

Do kopiowania obiektów możemy też użyć funkcji z modułu [`copy`](https://docs.python.org/3/library/copy.html):
* płytka kopia: [copy.copy](https://docs.python.org/3/library/copy.html#copy.copy)
* głęboka kopia: [copy.deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy)

Poniższe przykłady pokazują na czym polega płytka i głęboka kopia:

```python
import copy
```

#### Płytka kopia

```python
data = Data(2010, 5, 10)
osoba = Osoba("Jan", "Kowalski", data)
plytka_kopia = copy.copy(osoba)
```

Skopiowane są wszystkie pola, ale jeżeli pole jest referencją do obiektu (również listy, krotki), to skopiowana będzie referencja. W tym przypadku pole `data_urodzenia` typu `Data` będzie wspólne.

```python
plytka_kopia.imie = "Piotr"
```
Sprawdźmy:
```python
osoba.imie
```
Teraz dla pola zagnieżdżonego obiektu:
```python
plytka_kopia.data_urodzenia.dzien = 15
```
Sprawdźmy:
```python
osoba.data_urodzenia.dzien
```

**Sprawdź:**
* [Wizualizacja tworzenia płytkiej kopii obiektu w konstruktorze na stronie Python Tutor](https://pythontutor.com/visualize.html#code=import%20copy%0A%0A%0Aclass%20Data%3A%0A%20%20%20%20def%20__init__%28self,%20rok,%20miesiac,%20dzien%29%3A%0A%20%20%20%20%20%20%20%20self.rok%20%3D%20rok%0A%20%20%20%20%20%20%20%20self.miesiac%20%3D%20miesiac%0A%20%20%20%20%20%20%20%20self.dzien%20%3D%20dzien%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22Data%28%7Bself.rok!r%7D,%20%7Bself.miesiac!r%7D,%20%7Bself.dzien!r%7D%29%22%0A%0A%0Aclass%20Osoba%3A%0A%20%20%20%20%0A%20%20%20%20def%20__init__%28self,%20imie,%20nazwisko,%20data_urodzenia%29%3A%0A%20%20%20%20%20%20%20%20self.imie%20%3D%20imie%0A%20%20%20%20%20%20%20%20self.nazwisko%20%3D%20nazwisko%0A%20%20%20%20%20%20%20%20self.data_urodzenia%20%3D%20Data%28data_urodzenia.rok,%20data_urodzenia.miesiac,%20data_urodzenia.dzien%29%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22Osoba%28%7Bself.imie!r%7D,%20%7Bself.nazwisko!r%7D,%20%7Bself.data_urodzenia!r%7D%29%22%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%0A%0Adata%20%3D%20Data%282010,%205,%2010%29%0Aosoba%20%3D%20Osoba%28%22Jan%22,%20%22Kowalski%22,%20data%29%0Aplytka_kopia%20%3D%20copy.copy%28osoba%29%0A%0Aplytka_kopia.imie%20%3D%20%22Piotr%22%0Aprint%28osoba.imie%29%0A%0Aplytka_kopia.data_urodzenia.dzien%20%3D%2015%0Aprint%28osoba.data_urodzenia.dzien%29%0A%0A&curInstr=0&mode=display&origin=opt-frontend.js&py=3)

#### Głęboka kopia

```python
data = Data(2010, 5, 10)
osoba = Osoba("Jan", "Kowalski", data)
gleboka_kopia = copy.deepcopy(osoba)
```

```python
gleboka_kopia.imie = "Piotr"
```
Sprawdźmy:
```python
gleboka_kopia.imie
```
Teraz dla pola zagnieżdżonego obiektu:
```python
gleboka_kopia.data_urodzenia.dzien = 15
```
Sprawdźmy:
```python
osoba.data_urodzenia.dzien
```

W tym przypadku wszystko zostało skopiowane. Obiekt wskazywany przez `gleboka_kopia` nie ma żadnych danych wspólnych z obiektem `osoba`.

**Sprawdź:**
* [Wizualizacja tworzenia głębokiej kopii obiektu w konstruktorze na stronie Python Tutor](https://pythontutor.com/visualize.html#code=import%20copy%0A%0A%0Aclass%20Data%3A%0A%20%20%20%20def%20__init__%28self,%20rok,%20miesiac,%20dzien%29%3A%0A%20%20%20%20%20%20%20%20self.rok%20%3D%20rok%0A%20%20%20%20%20%20%20%20self.miesiac%20%3D%20miesiac%0A%20%20%20%20%20%20%20%20self.dzien%20%3D%20dzien%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22Data%28%7Bself.rok!r%7D,%20%7Bself.miesiac!r%7D,%20%7Bself.dzien!r%7D%29%22%0A%0A%0Aclass%20Osoba%3A%0A%20%20%20%20%0A%20%20%20%20def%20__init__%28self,%20imie,%20nazwisko,%20data_urodzenia%29%3A%0A%20%20%20%20%20%20%20%20self.imie%20%3D%20imie%0A%20%20%20%20%20%20%20%20self.nazwisko%20%3D%20nazwisko%0A%20%20%20%20%20%20%20%20self.data_urodzenia%20%3D%20Data%28data_urodzenia.rok,%20data_urodzenia.miesiac,%20data_urodzenia.dzien%29%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22Osoba%28%7Bself.imie!r%7D,%20%7Bself.nazwisko!r%7D,%20%7Bself.data_urodzenia!r%7D%29%22%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%0A%0Adata%20%3D%20Data%282010,%205,%2010%29%0Aosoba%20%3D%20Osoba%28%22Jan%22,%20%22Kowalski%22,%20data%29%0Agleboka_kopia%20%3D%20copy.deepcopy%28osoba%29%0A%0Agleboka_kopia.imie%20%3D%20%22Piotr%22%0Aprint%28osoba.imie%29%0A%0Agleboka_kopia.data_urodzenia.dzien%20%3D%2015%0Aprint%28osoba.data_urodzenia.dzien%29%0A%0A&curInstr=0&mode=display&origin=opt-frontend.js&py=3)

### Kopie innych struktur danych

Podobnie działa to np. dla list (oraz innych typów złożonych takich jak słowniki czy krotki).
Poniżej tworzymy listę, której ostatnim elementem jest również lista.

Tworzymy listę i jej płytką kopię:

```python
lista = [1, 2, [3, 4]]
kopia_listy = copy.copy(lista)
```
```python
kopia_listy
```
Lista została skopiowana, ale ostatni element (lista `[3, 4]`) jest wspólny:

```python
kopia_listy[0] = -1
kopia_listy[2][0] = -3
```
Sprawdźmy:
```python
kopia_listy
```

```python
lista
```

**Sprawdź:**
* [Wizualizacja płytkiej kopii listy na stronie Python Tutor](https://pythontutor.com/visualize.html#code=import%20copy%0A%0Alista%20%3D%20%5B1,%202,%20%5B3,%204%5D%5D%0A%0Akopia_listy%20%3D%20copy.copy%28lista%29%0A%0Akopia_listy%5B0%5D%20%3D%20-1%0Akopia_listy%5B2%5D%5B0%5D%20%3D%20-3%0A%0Aprint%28lista%29%0Aprint%28kopia_listy%29&curInstr=0&mode=display&origin=opt-frontend.js&py=3)


Teraz tworzymy głęboką kopię:

```python
lista = [1, 2, [3, 4]]
gleboka_kopia_listy = copy.deepcopy(lista)
```
Skopiowana lista nie ma żadnych wspólnych danych z listą.

```python
gleboka_kopia_listy[0] = -1
gleboka_kopia_listy[2][0] = -3
```

Sprawdźmy:
```python
gleboka_kopia_listy
```
```python
lista
```

**Sprawdź:**
* [Wizualizacja głębokiej kopii listy na stronie Python Tutor](https://pythontutor.com/visualize.html#code=import%20copy%0A%0Alista%20%3D%20%5B1,%202,%20%5B3,%204%5D%5D%0A%0Agleboka_kopia_listy%20%3D%20copy.deepcopy%28lista%29%0A%0Agleboka_kopia_listy%5B0%5D%20%3D%20-1%0Agleboka_kopia_listy%5B2%5D%5B0%5D%20%3D%20-3%0A%0Aprint%28lista%29%0Aprint%28gleboka_kopia_listy%29&curInstr=0&mode=display&origin=opt-frontend.js&py=3)


Definicja klasy `Osoba` używająca modułu `copy` mogłaby wyglądać tak:

```python
class Osoba:

    def __init__(self, imie, nazwisko, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = copy.copy(data_urodzenia)
```

Kopiujemy wyłącznie datę, która nie ma żadnych zagnieżdżonych struktur danych, więc wystarczy płytka kopia.