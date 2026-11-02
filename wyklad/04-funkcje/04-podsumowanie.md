# Parametry i argumenty funkcji — podsumowanie

## Terminologia

- parametr, argument
- argument pozycyjny i nazwany
- wartość domyślna

## Umiejętności i wiedza

- ustalanie na podstawie nagłówka funkcji, ile i jakich argumentów wymaga wywołanie, które parametry mają wartości domyślne oraz które wartości można przekazać pozycyjnie, jako nazwane albo na oba sposoby
- wywoływanie funkcji z argumentami pozycyjnymi i nazwanymi
- definiowanie parametrów, których wartości muszą być przekazywane jako argumenty nazwane
- definiowanie parametrów, których wartości muszą być przekazywane jako argumenty pozycyjne
- definiowanie funkcji przyjmujących dowolną liczbę argumentów pozycyjnych
- definiowanie funkcji przyjmujących dowolną liczbę argumentów nazwanych
- przekazywanie elementów sekwencji jako kolejnych argumentów pozycyjnych za pomocą gwiazdki na liście argumentów
- przekazywanie wpisów słownika jako argumentów nazwanych za pomocą dwóch gwiazdek na liście argumentów
- używanie mutowalnych obiektów, np. list, jako wartości domyślnych parametrów ze świadomością ich współdzielenia między wywołaniami oraz tworzenie osobnego obiektu dla każdego wywołania, gdy jest to potrzebne

## Ćwiczenia sprawdzające

Celem ćwiczeń jest samodzielne sprawdzenie zrozumienia materiału z wykładu i umiejętności użycia go. Jeżeli potrafisz je wykonać, masz podstawy do wykorzystania wiedzy z wykładu na laboratorium.

Jeżeli czegoś nie rozumiesz lub nie potrafisz wykonać, wróć do odpowiedniego fragmentu wykładu i spróbuj ponownie.

Część ćwiczeń zakłada wykonanie ich w trybie interaktywnym z załadowanymi odpowiednimi plikami źródłowymi. Możesz zamiast tego dopisać kod źródłowy wykonujący odpowiednie czynności i wyświetlający istotne informacje.

* [Przykładowe odpowiedzi do ćwiczeń](odpowiedzi-3)

### 1. Wartości domyślne i argumenty nazwane

Zdefiniuj funkcję `wynik(a, b=2, *, dodatek=0)`, która zwraca wartość wyrażenia `a * b + dodatek`.

Zastanów się, jakie będą wyniki poniższych wywołań. Następnie wykonaj je i sprawdź swoje przewidywania.

```python
wynik(3)
wynik(3, dodatek=4)
wynik(b=4, a=3)
```

### 2. Wymuszenie rodzaju argumentu

Zdefiniuj następującą funkcję:

```python
def roznica(a, /, *, b):
    return a - b
```

Zastanów się, które z poniższych wywołań są poprawne. Wyjaśnij rolę obu separatorów w nagłówku funkcji, a następnie sprawdź swoje przewidywania, wykonując każde wywołanie osobno.

```python
roznica(5, b=2)
roznica(a=5, b=2)
roznica(5, 2)
```

### 3. Dowolna liczba argumentów

Napisz funkcję `zbierz(*liczby, **opcje)`, która zwraca parę `(liczby, opcje)`. Zastanów się, jaki będzie wynik poniższego wywołania. Następnie wykonaj je i sprawdź swoje przewidywania.

```python
zbierz(1, 2, opis="test")
```

### 4. Rozpakowanie

Zdefiniuj następującą funkcję:

```python
def suma(a, b, c):
    return a + b + c
```

Napisz dwa wywołania tej funkcji. Pierwsze ma przekazywać elementy trójelementowej listy ze zmiennej `liczby` jako kolejne argumenty pozycyjne. Drugie ma przekazywać wpisy słownika ze zmiennej `skladniki`, z kluczami `"a"`, `"b"` i `"c"`, jako argumenty nazwane. Nie przepisuj osobno trzech wartości w wywołaniu.

Sprawdź swoje wywołania po wykonaniu poniższych przypisań:

```python
liczby = [1, 2, 3]
skladniki = {"a": 1, "b": 2, "c": 3}
```

### 5. Mutowalna wartość domyślna

Zdefiniuj następującą funkcję:

```python
def dodaj(x, lista=[]):
    lista.append(x)
    return lista
```

Wykonaj kolejno wywołania `dodaj(1)` i `dodaj(2)` i sprawdź zawartość zwróconych list. Zmień definicję funkcji tak, żeby każde wywołanie bez drugiego argumentu tworzyło osobną listę. Ponownie wykonaj oba wywołania i sprawdź, czy uzyskujesz odpowiednio listy `[1]` i `[2]`.
