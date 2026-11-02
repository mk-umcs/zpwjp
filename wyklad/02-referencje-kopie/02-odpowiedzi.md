# Odpowiedzi do ćwiczeń

Przykładowe odpowiedzi. W ćwiczeniach 1–4 używamy początkowych definicji `Polozenie` i `Czujnik` z podsumowania. Dopiero ćwiczenie 5 zmienia konstruktor.

## 1. Dwie zmienne, jeden obiekt

```python-repl
>>> pozycja1 = Polozenie(10, 20, 30)
>>> pozycja2 = pozycja1
>>> pozycja1 is pozycja2
True
>>> pozycja2.z = 35
>>> pozycja1.z
35
```

## 2. Wspólne pole dwóch obiektów

```python-repl
>>> pozycja = Polozenie(10, 20, 30)
>>> pierwszy = Czujnik("T1", "A", pozycja)
>>> drugi = Czujnik("T2", "A", pozycja)
>>> pierwszy is drugi
False
>>> pierwszy.polozenie is drugi.polozenie
True
>>> drugi.polozenie.z = 35
>>> pierwszy.polozenie
Polozenie(10, 20, 35)
>>> pozycja
Polozenie(10, 20, 35)
```

## 3. Płytka kopia

```python-repl
>>> import copy
>>> pierwszy = Czujnik("T1", "A", Polozenie(10, 20, 30))
>>> kopia = copy.copy(pierwszy)
>>> kopia is pierwszy
False
>>> kopia.polozenie is pierwszy.polozenie
True
>>> kopia.nazwa = "T3"
>>> kopia.polozenie.z = 35
>>> pierwszy.nazwa
'T1'
>>> pierwszy.polozenie
Polozenie(10, 20, 35)
```

Powstał nowy obiekt `Czujnik`, ale oba pola `polozenie` nadal wskazują ten sam obiekt. Przypisanie do `kopia.nazwa` zmienia pole tylko w kopii, ale zmiana współrzędnej `z` dotyczy wspólnego położenia.

## 4. Głęboka kopia

```python-repl
>>> import copy
>>> pierwszy = Czujnik("T1", "A", Polozenie(10, 20, 30))
>>> kopia = copy.deepcopy(pierwszy)
>>> kopia is pierwszy
False
>>> kopia.polozenie is pierwszy.polozenie
False
>>> kopia.nazwa = "T3"
>>> kopia.polozenie.z = 35
>>> pierwszy.nazwa
'T1'
>>> pierwszy.polozenie
Polozenie(10, 20, 30)
```

Skopiowany został również obiekt położenia. Zmiana jego pól nie zmienia położenia w oryginale.

## 5. Kopia w konstruktorze

```python
class Czujnik:
    def __init__(self, nazwa, model, polozenie):
        self.nazwa = nazwa
        self.model = model
        self.polozenie = Polozenie(
            polozenie.x, polozenie.y, polozenie.z
        )
```

Po wykonaniu tej definicji utwórz nowe obiekty:

```python-repl
>>> pozycja = Polozenie(10, 20, 30)
>>> pierwszy = Czujnik("T1", "A", pozycja)
>>> drugi = Czujnik("T2", "A", pozycja)
>>> pierwszy.polozenie is drugi.polozenie
False
>>> pierwszy.polozenie is pozycja
False
>>> drugi.polozenie.z = 35
>>> drugi.polozenie
Polozenie(10, 20, 35)
>>> pierwszy.polozenie
Polozenie(10, 20, 30)
>>> pozycja
Polozenie(10, 20, 30)
```