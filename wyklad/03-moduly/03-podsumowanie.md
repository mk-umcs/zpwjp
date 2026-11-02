# Moduły i argumenty wiersza polecenia — podsumowanie

## Umiejętności i wiedza

- utworzenie modułu zawierającego definicje klas i funkcji i używanie go w programach
- rozróżnienie, czy kod wykonuje się z powodu importu, czy bezpośredniego uruchomienia pliku, w którym się znajduje
- zrozumienie korzyści z podziału większego programu na moduły
- uzyskanie informacji o liczbie i wartościach argumentów wiersza polecenia za pomocą [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv)

## Ćwiczenia sprawdzające

Celem ćwiczeń jest samodzielne sprawdzenie zrozumienia materiału z wykładu i umiejętności użycia go. Jeżeli potrafisz je wykonać, masz podstawy do wykorzystania wiedzy z wykładu na laboratorium.

Jeżeli czegoś nie rozumiesz lub nie potrafisz wykonać, wróć do odpowiedniego fragmentu wykładu i spróbuj ponownie.

Część ćwiczeń zakłada wykonanie ich w trybie interaktywnym z załadowanymi odpowiednimi plikami źródłowymi. Możesz zamiast tego dopisać kod źródłowy wykonujący odpowiednie czynności i wyświetlający istotne informacje.

* [Przykładowe odpowiedzi do ćwiczeń](odpowiedzi-2)

### 1. Moduł i korzystający z niego program

Napisz moduł `kwadrat.py` z funkcjami obliczającymi pole i obwód kwadratu o podanym boku. Dodaj kod wyświetlający w osobnych wierszach bok, pole i obwód kwadratu o boku 2, wykonywany wyłącznie przy bezpośrednim uruchomieniu modułu.

Napisz osobny program korzystający z tego modułu. Program ma pobierać od użytkownika bok i wyświetlać w czytelny sposób bok, pole i obwód. Sprawdź, czy import modułu nie uruchamia kodu wyświetlającego informacje dla kwadratu o boku 2 zawartego w module.

### 2. Dwa argumenty

Załóż, że program uruchomiono poleceniem `python proba.py dane.txt 3`. Zastanów się, jaka będzie zawartość `sys.argv`. Jak sprawdzić, czy w wywołaniu podano drugi argument po nazwie skryptu? Jak uzyskać jego wartość i jaki będzie jej typ w tym przykładzie? Sprawdź odpowiedzi w krótkim programie.
