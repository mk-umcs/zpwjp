# Polimorfizm i dziedziczenie — podsumowanie

## Terminologia

- polimorfizm
- duck typing
- dziedziczenie
- klasa bazowa i pochodna
- nadpisanie metody
- klasa abstrakcyjna i konkretna

## Umiejętności i wiedza

- używanie wspólnej operacji dla różnych typów
- dziedziczenie i nadpisywanie metod
- rozróżnianie sprawdzenia dokładnego typu i isinstance
- rozpoznawanie roli metod abstrakcyjnych i hierarchii wyjątków

## Ćwiczenia sprawdzające

Celem ćwiczeń jest samodzielne sprawdzenie zrozumienia materiału z wykładu i umiejętności użycia go. Jeżeli potrafisz je wykonać, masz podstawy do wykorzystania wiedzy z wykładu na laboratorium.

Jeżeli czegoś nie rozumiesz lub nie potrafisz wykonać, wróć do odpowiedniego fragmentu wykładu i spróbuj ponownie.

Część ćwiczeń zakłada wykonanie ich w trybie interaktywnym z załadowanymi odpowiednimi plikami źródłowymi. Możesz zamiast tego dopisać kod źródłowy wykonujący odpowiednie czynności i wyświetlający istotne informacje.

* [Przykładowe odpowiedzi do ćwiczeń](odpowiedzi-5)

### 1. Wspólna metoda bez dziedziczenia

Zdefiniuj dwie klasy: `Bilet` i `Produkt`. Każda z nich ma mieć metodę `cena`, która zwraca cenę jednego biletu lub jednej sztuki produktu: odpowiednio `10` i `7`.

Napisz funkcję `koszt(element, liczba)`, która oblicza łączny koszt podanej liczby biletów lub sztuk produktu, korzystając z metody `cena` przekazanego obiektu. Utwórz po jednym obiekcie każdej klasy i wywołaj dla nich tę funkcję, obliczając koszt dziesięciu biletów oraz dziesięciu sztuk produktu.

Czy obie klasy muszą dziedziczyć po wspólnej, zdefiniowanej przez Ciebie klasie bazowej, żeby funkcja mogła z nich korzystać?

### 2. Nadpisanie metody

Zdefiniuj klasę `BiletUlgowy` dziedziczącą po klasie `Bilet` z poprzedniego ćwiczenia. Nadpisz metodę `cena` tak, żeby zwracała połowę ceny otrzymanej z metody klasy bazowej, wywołanej za pomocą [`super`](https://docs.python.org/3/library/functions.html#super). Utwórz obiekt klasy `BiletUlgowy`, wywołaj jego metodę `cena` i sprawdź wynik.

### 3. Typ dokładny a zgodność z klasą bazową

Utwórz obiekt klasy `BiletUlgowy` z poprzedniego ćwiczenia i przypisz go do zmiennej `ulgowy`:

```python
ulgowy = BiletUlgowy()
```

Zastanów się, jakie wyniki dadzą poniższe wyrażenia. Następnie oblicz ich wartości i sprawdź swoje przewidywania.

```python
type(ulgowy) is Bilet
isinstance(ulgowy, Bilet)
```

### 4. Niepełna implementacja klasy abstrakcyjnej

Załóż, że klasa `Usluga` dziedziczy po [`abc.ABC`](https://docs.python.org/3/library/abc.html#abc.ABC) i ma metodę `cena` oznaczoną dekoratorem [`abc.abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod). Klasa `Dostawa` dziedziczy po klasie `Usluga`, ale nie implementuje tej metody.

Czy można utworzyć obiekt klasy `Dostawa` przez wywołanie `Dostawa()`? Jeżeli nie, wyjaśnij, co trzeba uzupełnić w tej klasie.

### 5. Hierarchia wyjątków

Zdefiniuj klasę wyjątku `BladCeny` dziedziczącą po klasie [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError). Napisz blok `try`, w którym zgłosisz wyjątek tej klasy z komunikatem `"ujemna cena"`, oraz klauzulę `except ValueError` wyświetlającą komunikat o jego wyłapaniu.

Zastanów się, czy wyjątek zostanie wyłapany. Następnie wykonaj kod i sprawdź swoje przewidywania.
