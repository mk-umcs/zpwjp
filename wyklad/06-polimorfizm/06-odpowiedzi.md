# Odpowiedzi do ćwiczeń

Przykładowe odpowiedzi. Istotny jest efekt działania kodu; inne poprawne rozwiązania również są możliwe.

## 1. Wspólna metoda bez dziedziczenia

```python
class Bilet:
    def cena(self):
        return 10


class Produkt:
    def cena(self):
        return 7


def koszt(element, liczba):
    return element.cena() * liczba
```

```python-repl
>>> koszt(Bilet(), 10)
100
>>> koszt(Produkt(), 10)
70
```

Funkcja korzysta z metody `cena` obu obiektów i mnoży otrzymaną cenę jednostkową przez liczbę sztuk. Wystarczy, że każda klasa udostępnia potrzebną metodę; nie trzeba definiować dla nich wspólnej klasy bazowej.

## 2. Nadpisanie metody

```python
class BiletUlgowy(Bilet):
    def cena(self):
        return super().cena() / 2
```

```python-repl
>>> BiletUlgowy().cena()
5.0
```

## 3. Typ dokładny a zgodność z klasą bazową

```python-repl
>>> ulgowy = BiletUlgowy()
>>> type(ulgowy) is Bilet
False
>>> isinstance(ulgowy, Bilet)
True
```

Dokładny typ obiektu to `BiletUlgowy`. Ponieważ ta klasa dziedziczy po klasie `Bilet`, sprawdzenie za pomocą funkcji `isinstance` również uznaje obiekt za obiekt klasy `Bilet`.

## 4. Niepełna implementacja klasy abstrakcyjnej

Próba utworzenia `Dostawa()` spowoduje [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError). Klasa pozostaje abstrakcyjna, dopóki nie dostarczy implementacji wymaganej metody `cena` (bezpośrednio lub przez odpowiednią klasę pośrednią).

## 5. Hierarchia wyjątków

```python
class BladCeny(ValueError):
    pass
```

```python-repl
>>> try:
...     raise BladCeny("ujemna cena")
... except ValueError:
...     print("Wyłapano")
Wyłapano
```

Klauzula obejmuje również wyjątki klas pochodnych od [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError).
