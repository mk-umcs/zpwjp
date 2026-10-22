---

### Zadanie 1.3. Różne rozszerzenia modułu i klasy

Rozwiń moduł o nowe funkcje, a następnie rozbuduj klasę o metody z nich korzystające.

**Uwaga:** Metody w klasie nie modyfikować obiektu (pól `tablica`, `wysokosc` i `szerokosc`), na którym zostały wywołane. W razie potrzeby metoda powinna zwrócić nowy obiekt klasy `Raster`.

Dodaj w module funkcje realizujące:
1. odczyt i zapis z CSV,
2. obliczenie mody (wartości najczęstszej) &mdash; w przypadku wielu takich wartości funkcja może zwrócić dowolną wybraną, lub zwrócić kompletną listę takich wartości (wybierz sposób),
3. zmniejszenie rastra o zadaną liczbę komórek z każdej strony (obcinanie brzegów),
4. kompresja rastra - zmniejszenie rozdzielczości (np. z okna 2x2 komórek powstaje 1 komórka z wartością średnią). Komórki na niepełnych brzegach są ignorowane. W klasie metoda `kompresuj(self, okno)`, zwracająca nową instancję rastra.
5. **Operacje z maską**. Metody statystyczne przyjmujące dodatkowy obiekt klasy `Raster` (maskę). Do obliczeń brane są pod uwagę tylko te pola z bieżącego rastra, na których odpowiadających pozycjach maska posiada wartość potraktowaną jako `True` (różną od 0).

---

## Część IV: Program główny i argumenty wiersza poleceń

Utwórz oddzielny plik (np. `main.py`), który zaimportuje klasę i/lub funkcje z Twojego modułu.

1. Wykorzystaj moduł `sys` i sprawdź zawartość `sys.argv`.
2. Jeżeli program został uruchomiony z parametrem wiersza poleceń (np. `python main.py dane.csv`), potraktuj pierwszy argument jako ścieżkę do pliku tekstowego i z niego wczytaj raster.
3. Jeżeli programu użyto bez argumentów, wymuś ręczne wczytanie rastra od użytkownika (np. poprzez Twoją funkcję narzędziową).
4. Następnie utwórz z tych danych obiekt `Raster` i wyświetl w pętli menu tekstowe pozwalające użytkownikowi na wielokrotne wybieranie i wykonywanie przygotowanych operacji (wyświetlenie statystyk, wyświetlenie danych, zapisanie, itp.). W przypadku błędu odczytu (wyjątki zgłoszone z modułu/klasy) program powinien wypisać sensowny komunikat i się zakończyć.

---

## Część V: Wyzwanie – stan obiektu i aktualizacja danych

W ramach alternatywnego podejścia do obliczeń statystycznych rozważ wprowadzenie do klasy tzw. "pamięci stanu" (buforowania).

1. Napisz funkcję (w module proceduralnym), która jednorazowo iteruje po danych i zwraca **krotkę z czterema wartościami** (min, max, średnia, moda).
2. Dodaj do klasy `Raster` nowe pole `bufor_statystyk` i zainicjalizuj je w konstruktorze jako `None`.
3. Dodaj w klasie metodę `oblicz_statystyki(self)`, która pod spodem wywoła nową funkcję obliczającą, ale **nic nie zwróci** – zamiast tego zapisze otrzymaną krotkę do pola `bufor_statystyk`.
4. Zmień metody `najmniejsza_wartosc(self)`, `srednia(self)` itd. w taki sposób, aby przestały na bieżąco uruchamiać obliczenia. Zamiast tego mają odczytywać z góry określone indeksy z zapisanej w polu `bufor_statystyk` krotki. Jeśli w momencie odpytania to pole wynosi `None`, metody powinny rzucić wyjątek `ValueError` z informacją ("Statystyki nie zostały jeszcze policzone").

**Problem do zastanowienia:** Jeśli użytkownik po użyciu `oblicz_statystyki()` bezpośrednio zmodyfikuje zawartość pola `tablica` (np. przypisując `moj_raster.tablica[0][0] = 999.0`), metody z Części V zwrócą **nieaktualne, fałszywe wyniki**, dopóki ktoś nie wymusi ponownego przeliczenia. Jak widzisz, jawny dostęp do atrybutów bywa ryzykowny – jak można by temu zapobiec, aby obiekt sam kontrolował zmiany swoich danych? Zastanów się nad tym przed kolejnym wykładem!
