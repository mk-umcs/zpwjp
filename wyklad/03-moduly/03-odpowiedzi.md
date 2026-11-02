# Odpowiedzi do ćwiczeń

## 1. Moduł i korzystający z niego program

Plik `kwadrat.py`:

```python
def pole(bok):
    return bok ** 2


def obwod(bok):
    return 4 * bok


def main():
    bok = 2
    print(bok)
    print(pole(bok))
    print(obwod(bok))


if __name__ == "__main__":
    main()
```

Osobny program:

```python
import kwadrat


def main():
    bok = float(input("Bok kwadratu: "))
    print("bok:", bok)
    print("pole:", kwadrat.pole(bok))
    print("obwód:", kwadrat.obwod(bok))


if __name__ == "__main__":
    main()
```

## 2. Dwa argumenty

Zmienna `sys.argv` ma wartość `["proba.py", "dane.txt", "3"]`.

Drugi argument po nazwie skryptu istnieje, gdy `len(sys.argv) > 2`. Wtedy odczytamy go przez `sys.argv[2]`. W pokazanym wywołaniu ma wartość `"3"` i typ `str`.

```python
import sys

if len(sys.argv > 2):
    print(f"Podano drugi argument: {sys.argv[2]}.")
else:
    print("Nie podano drugiego argumentu.")
```
