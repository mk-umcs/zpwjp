# Odpowiedzi do ćwiczeń

Przykładowe odpowiedzi. Istotny jest efekt działania kodu; inne poprawne rozwiązania również są możliwe.

## 1. Wartości domyślne i argumenty nazwane

```python
def wynik(a, b=2, *, dodatek=0):
    return a * b + dodatek
```

```python-repl
>>> wynik(3)
6
>>> wynik(3, dodatek=4)
10
>>> wynik(b=4, a=3)
12
```

## 2. Wymuszenie rodzaju argumentu

Poprawne jest tylko wywołanie `roznica(5, b=2)`. Parametr `a` przed separatorem `/` wymaga argumentu pozycyjnego, a parametr `b` po separatorze `*` wymaga argumentu nazwanego. Dlatego drugie wywołanie jest błędne, ponieważ przekazuje wartość parametru `a` jako argument nazwany, a trzecie — ponieważ przekazuje wartość parametru `b` jako argument pozycyjny.

## 3. Dowolna liczba argumentów

```python
def zbierz(*liczby, **opcje):
    return liczby, opcje
```

```python-repl
>>> zbierz(1, 2, opis="test")
((1, 2), {'opis': 'test'})
```

## 4. Rozpakowanie

```python
def suma(a, b, c):
    return a + b + c
```

```python-repl
>>> liczby = [1, 2, 3]
>>> skladniki = {"a": 1, "b": 2, "c": 3}
>>> suma(*liczby)
6
>>> suma(**skladniki)
6
```

## 5. Mutowalna wartość domyślna

```python
def dodaj(x, lista=None):
    if lista is None:
        lista = []
    lista.append(x)
    return lista
```

```python-repl
>>> dodaj(1)
[1]
>>> dodaj(2)
[2]
```
