# Odpowiedzi do ćwiczeń

Przykładowe odpowiedzi. Istotny jest efekt działania kodu; inne poprawne rozwiązania również są możliwe.

W przykładach używamy klasy `Poziom` z podsumowania.

## 1. Odczyt i zapis właściwości

```python-repl
>>> poziom = Poziom(25)
>>> poziom.procent, poziom.ulamek
(25, 0.25)
>>> poziom.procent = 40
>>> poziom.procent, poziom.ulamek
(40, 0.4)
```

Odczyt i zapis mają postać operacji na polu, bez nawiasów wywołania. Getter i setter zostają wywołane przez mechanizm właściwości.

## 2. Walidacja

```python-repl
>>> poziom = Poziom(25)
>>> try:
...     poziom.procent = 120
... except ValueError:
...     print("Błędna wartość")
Błędna wartość
>>> poziom.procent
25
```

Sprawdzenie w setterze poprzedza przypisanie, więc stan pozostaje poprawny.

## 3. Właściwość tylko do odczytu

```python-repl
>>> poziom = Poziom(25)
>>> try:
...     poziom.ulamek = 0.5
... except AttributeError:
...     print("Brak settera")
Brak settera
```

Właściwość `ulamek` nie ma zdefiniowanego settera.

## 4. Interfejs a reprezentacja

Publiczne właściwości to `procent` i `ulamek`. Pole `_procent` jest niepublicznym szczegółem implementacji. Bezpośrednie przypisanie do niego omija setter, w tym sprawdzenie zakresu. Podkreślenie jest konwencją, a nie techniczną blokadą dostępu.
