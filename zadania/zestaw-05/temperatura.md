# Właściwości i walidacja: temperatura

## 1. Klasa `Temperatura`

Temperaturę można podawać m\.in. w [skali Celsjusza](https://pl.wikipedia.org/wiki/Skala_Celsjusza) i [skali Fahrenheita](https://pl.wikipedia.org/wiki/Skala_Fahrenheita). Stwórz klasę `Temperatura`, której obiekty reprezentują temperaturę. Obiekty tworzone są na podstawie temperatury w stopniach Celsjusza. Nie można utworzyć obiektu z wartością poniżej zera absolutnego.

```pycon
>>> t1 = Temperatura(36.7)
>>> t2 = Temperatura(-300)
Traceback (most recent call last):
...
ValueError: temperatura poniżej zera absolutnego
```

Obiekty klasy mają pole `celsjusz` i właściwość do odczytu `fahrenheit`:

```pycon
>>> t1.celsjusz
36.7
>>> t1.fahrenheit
98.06
>>> t1.celsjusz = 0.0
>>> t1.fahrenheit
32.0
>>> t1.fahrenheit = 100
...
AttributeError: can't set attribute
```

Czy można utworzyć obiekt typu `Temperatura` z temperaturą poniżej zera absolutnego przez utworzenie obiektu z dowolną temperaturą i podstawienie np. wartości `-300` pod pole `celsjusz`?

Napisz program wyświetlający temperatury 0°C, 10°C, ..., 90°C, 100°C w stopniach Fahrenheita.

**Przydatne odnośniki:**

- [Przeliczanie temperatur](https://pl.wikipedia.org/wiki/Skala_Fahrenheita#Przeliczanie)
- [Zero absolutne](https://pl.wikipedia.org/wiki/Zero_bezwzgl%C4%99dne)

## 2. Klasa `Temperatura` &mdash; modyfikacja obiektu za pomocą właściwości, zabezpieczenie przed błędną temperaturą

Zmodyfikuj klasę `Temperatura` w taki sposób, żeby:

- była możliwa zmiana temperatury przez ustawienie stopni Fahrenheita,
- nie było możliwe utworzenie obiektu z temperaturą poniżej zera absolutnego również za pomocą podstawienia.

```pycon
>>> t = Temperatura(100)
>>> t.fahrenheit
212.0
>>> t.fahrenheit = 200.0
>>> t.celsjusz
93.33333333333334
>>> t.celsjusz = -300
...
ValueError: temperatura poniżej zera absolutnego
>>> t.fahrenheit = -500
...
ValueError: temperatura poniżej zera absolutnego
```

## 3. Klasa `Temperatura` &mdash; tworzenie obiektu na podstawie stopni `Fahrenheita`

Zmodyfikuj metodę `__init__` w klasie `Temperatura` tak, żeby możliwe było utworzenie obiektu temperatura również na podstawie stopni Fahrenheita. Możliwe mają być następujące sposoby utworzenia obiektu:

```pycon
>>> t1 = Temperatura(100.0)
>>> t2 = Temperatura(celsjusz=100.0)    # równoważne z poprzednim
>>> t3 = Temperatura(fahrenheit=212.0)
```

a następujące wywołania mają powodować zgłoszenie wyjątku `TypeError`:

```pycon
>>> t4 = Temperatura()
...
TypeError: brak argumentów
>>> t5 = Temperatura(celsjusz=100.0, fahrenheit=100.0)
...
TypeError: za dużo argumentów
```

Napisz program wyświetlający temperatury 0°F, 10°F, ..., 90°F, 100°F w stopniach Celsjusza.

## 4. Klasa `Temperatura` &mdash; dodatkowe zadania

- Zastanów się nad rozszerzeniem klasy `Temperatura` o informacje o czasie i przestrzeni tak, żeby obiekty klasy oprócz temperatury mogły przechowywać również informacje o czasie i miejscu pomiaru temperatury. Rozważ użycie dziedziczenia i zaimplementowanie dodatkowej klasy pochodnej (lub klas pochodnych) klasy `Temperatura`. Zaprojektuj w odpowiedni sposób konstruktory i pozostałe składowe napisanych klas.

- Zastanów się nad innym niż w zadaniu trzecim sposobem tworzenia temperatury na podstawie stopni Fahrenheita, np. za pomocą odpowiedniej metody klasy (`classmethod`).

    Zastanów się nad dodaniem możliwości konstruowania temperatury z użyciem innych skal, np. skali Kelvina, czy skali Rankine'a oraz dodaniem odpowiednich właściwości `kelwin` i `rankine`.
    
    Czy według ciebie dodanie obsługi tych skal podczas konstruowania obiektu jest łatwiejsze z użyciem parametru nazwanego, czy za pomocą metod klasy. Który z tych sposobów wymaga poprawienia istniejącej metody lub metod, a który wymaga tylko dopisania nowej metody (lub nowych metod), ale bez modyfikowania żadnej z już napisanych metod.

    **Przydatne odnośniki:**

    - [Skala Kelvina](https://pl.wikipedia.org/wiki/Kelwin)
    - [skala Rankine'a](https://pl.wikipedia.org/wiki/Skala_Rankine%E2%80%99a)
