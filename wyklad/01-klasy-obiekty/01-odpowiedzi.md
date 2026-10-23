# Odpowiedzi do ćwiczeń

Przykładowe odpowiedzi do ćwiczeń:

1.

```python
class Wspolrzedne:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
```

2.

```python-repl
>>> lublin = Wspolrzedne(22.57, 51.25)
>>> lublin.dlugosc
22.57
>>> lublin.szerokosc
51.25
```

3.

```python-repl
>>> lublin.dlugosc = 33.57
>>> lublin.dlugosc
33.57
>>> lublin.dlugosc = 22.57
>>> lublin.szerokosc = 50.5
>>> lublin.szerokosc
50.5
>>> lublin.szerokosc = 51.25
```

4.

```python-repl
>>> warszawa = Wspolrzedne(21.01, 52.23)
>>> lublin.dlugosc - warszawa.dlugosc
1.5599999999999987
>>> lublin.szerokosc < warszawa.szerokosc
True
```

5.

```python
class Wspolrzedne:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def polkula_polnocna(self):
        return self.szerokosc > 0
```

6.

```python-repl
>>> p1 = Wspolrzedne(10.0, -10.0)
>>> p2 = Wspolrzedne(10.0, 0.0)
>>> p3 = Wspolrzedne(10.0, 10.0)
>>> p1.polkula_polnocna()
False
>>> p2.polkula_polnocna()
False
>>> p3.polkula_polnocna()
True
>>> p1.szerokosc = 10.0
>>> p1.polkula_polnocna()
True
>>> p1.szerokosc = 0.0
>>> p1.polkula_polnocna()
False
```

7. Metody `__repr__` i `__str__`

```python
class Wspolrzedne:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def polkula_polnocna(self):
        return self.szerokosc > 0

    def __repr__(self):
        return f"Wspolrzedne({self.dlugosc!r}, {self.szerokosc!r})"

    def __str__(self):
        return f"({self.dlugosc}\u00b0, {self.szerokosc}\u00b0)"
```
