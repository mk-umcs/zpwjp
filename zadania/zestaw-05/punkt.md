# Właściwości punktu: stopnie i promień

Napisz klasę `Punkt` reprezentującą punkt na płaszczyźnie. Konstruktor ma dwa parametry — współrzędne kartezjańskie. Przekazanie do konstruktora wartości typu innego niż `float` lub `int` kończy się zgłoszeniem odpowiedniego wyjątku.

Klasa ma cztery właściwości:

- `x` i `y` — współrzędne kartezjańskie; właściwości do zapisu i do odczytu; próba podstawienia wartości typu innego niż `float` lub `int` kończy się zgłoszeniem odpowiedniego wyjątku,

- `promien` i `kat` (w stopniach) — [współrzędne biegunowe](https://pl.wikipedia.org/wiki/Uk%C5%82ad_wsp%C3%B3%C5%82rz%C4%99dnych_biegunowych) — właściwości tylko do odczytu; wskazówka: kąt można policzyć za pomocą funkcji [`math.atan2`](https://docs.python.org/3/library/math.html#math.atan2) jako `atan2(y, x)`; przeliczenie na stopnie można wykonać za pomocą funkcji [`math.degrees`](https://docs.python.org/3/library/math.html#math.degrees).

Przykład użycia klasy:


```pycon
>>> p = Punkt(3, 4)
>>> p.kat
53.13010235415598
>>> p.promien
5.0
>>> p = Punkt(-1, 1)
>>> p.promien
1.4142135623730951
>>> p.kat
135.0
>>> p.x = 0
>>> p.kat
90.0
>>> p.promien
1.0
>>> p.promien = 10
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
>>> p = Punkt('3', 5)
...
TypeError: błędny typ
>>> p = Punkt(0, 0)
>>> p.y = [1, 2, 3]
...
TypeError: błędny typ
```
