# Abstrakcja i enkapsulacja — podsumowanie

## Terminologia

- abstrakcja, publiczny interfejs
- enkapsulacja (hermetyzacja)
- właściwość (property)

## Umiejętności i wiedza

- wyjaśnienie, jak podział składowych na publiczne i niepubliczne pomaga chronić poprawny stan obiektu oraz zmieniać wewnętrzną reprezentację bez zmiany sposobu używania klasy
- rozumienie konsekwencji udostępnienia zwykłych pól jako publicznych: kod korzystający z klasy może bezpośrednio zmieniać ich wartości, omijając sprawdzenia w metodach, i uzależnia się od sposobu przechowywania danych
- znajomość konwencji nazywania składowych niepublicznych w Pythonie i świadomość, że nie blokuje ona technicznie dostępu
- przestrzeganie zasady używania składowych niepublicznych tylko w implementacji klasy, a publicznego interfejsu w kodzie korzystającym z klasy
- definiowanie właściwości tylko do odczytu oraz właściwości umożliwiających odczyt i zapis za pomocą gettera i settera

## Ćwiczenia sprawdzające

Celem ćwiczeń jest samodzielne sprawdzenie zrozumienia materiału z wykładu i umiejętności użycia go. Jeżeli potrafisz je wykonać, masz podstawy do wykorzystania wiedzy z wykładu na laboratorium.

Jeżeli czegoś nie rozumiesz lub nie potrafisz wykonać, wróć do odpowiedniego fragmentu wykładu i spróbuj ponownie.

Część ćwiczeń zakłada wykonanie ich w trybie interaktywnym z załadowanymi odpowiednimi plikami źródłowymi. Możesz zamiast tego dopisać kod źródłowy wykonujący odpowiednie czynności i wyświetlający istotne informacje.

* [Przykładowe odpowiedzi do ćwiczeń](odpowiedzi-4)


### Wprowadzenie

W ćwiczeniach 1–3 skorzystaj z klasy:

```python
class Poziom:
    def __init__(self, procent):
        self.procent = procent

    @property
    def procent(self):
        return self._procent

    @procent.setter
    def procent(self, wartosc):
        if not 0 <= wartosc <= 100:
            raise ValueError("poza zakresem")
        self._procent = wartosc

    @property
    def ulamek(self):
        return self._procent / 100

```

### 1. Odczyt i zapis właściwości

Utwórz obiekt klasy `Poziom` z początkową wartością procentową równą `25` i przypisz go do zmiennej `poziom`. Odczytaj wartości właściwości `procent` i `ulamek` tego obiektu. Następnie przypisz wartość `40` do właściwości `procent` i ponownie odczytaj obie właściwości. Czy przy odczycie właściwości używamy nawiasów tak jak przy wywołaniu metody?

### 2. Walidacja

Utwórz nowy obiekt klasy `Poziom` z początkową wartością procentową równą `25` i przypisz go do zmiennej `poziom`. Następnie spróbuj przypisać wartość `120` do właściwości `procent` tego obiektu. Jaki wyjątek wystąpi? Po tej próbie odczytaj wartość właściwości `procent` i sprawdź, czy została zmieniona.

### 3. Właściwość tylko do odczytu

Utwórz obiekt klasy `Poziom` z początkową wartością procentową równą `25` i przypisz go do zmiennej `poziom`. Odczytaj wartość jego właściwości `ulamek`, a następnie spróbuj wykonać instrukcję podstawienia `poziom.ulamek = 0.5`. Dlaczego przypisanie nowej wartości nie jest możliwe, chociaż odczyt działa?

### 4. Interfejs a reprezentacja

Wskaż, które składowe klasy `Poziom` tworzą jej publiczny interfejs, a która składowa jest niepublicznym polem przechowującym dane. Czy kod korzystający z klasy powinien przypisywać wartości bezpośrednio do pola `_procent`? Wyjaśnij, jakie sprawdzenie poprawności danych zostałoby wtedy pominięte.
