# Prostokąt i kwadrat — odpowiedzi do ćwiczeń

## 1. Relacja klas i umowa

`isinstance` sprawdza przynależność do klasy lub jej podklasy. Nie sprawdza, czy nadpisana metoda zachowuje umowę klasy bazowej. Klasa `Kwadrat` dziedziczy po `Prostokat`, ale zmiana wysokości zmienia w niej również szerokość.

## 2. Oczekiwanie obliczone po zmianie

Funkcja przeoczy problem: dla kwadratu szerokość po operacji wynosi `10`, więc oczekiwane pole obliczy jako `10 * 10`. Wynik `100` będzie się zgadzał z polem obiektu. Tymczasem właściwe oczekiwanie wynikało z wcześniejszej szerokości `5` i wynosiło `50`.

## 3. Usunięcie metod

Nie wystarczy. Pierwsza klasa przechowuje publiczne pola, którym wciąż można przypisywać nowe wartości, np. `prostokat.wysokosc = 10`. Trzeba określić cały publiczny interfejs i dostępne operacje, a nie tylko nazwy metod.

## 4. Nowa figura

```python
kwadrat = KwadratVO(5)
wynik = kwadrat.z_szerokoscia(8)
print(wynik)
print(kwadrat)
```

Otrzymamy `ProstokatVO(8x5)` oraz niezmieniony `KwadratVO(5x5)`. Wynik jest klasy `ProstokatVO`; operacja nie obiecywała zachowania typu kwadratu.

## 5. Porównywanie wartości

W tym modelu obie figury reprezentują tę samą parę wymiarów, więc porównanie `==` daje `True`. Decyduje odziedziczona metoda `ProstokatVO.__eq__`. Obiekty utworzone przez dwa wywołania konstruktora pozostają odrębne: porównanie `is` daje `False`.

Inny model mógłby oprócz wymiarów uwzględniać również inne cechy. Regułę równości trzeba wtedy określić odpowiednio do tego modelu.
