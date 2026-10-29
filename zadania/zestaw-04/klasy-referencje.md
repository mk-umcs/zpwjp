# Współpraca obiektów i kopie

**Uwaga:** Sformułowanie &bdquo;Napisz klasę `Nazwa(parametry)`&rdquo; oznacza utworzenie klasy `Nazwa`, której konstruktor (metoda `__init__`) przyjmuje podane parametry, oprócz `self`. Nie mówi to nic o składni definicji klasy.

(licznik-slow)=
## 1. Licznik słów

Napisz klasę `LicznikSlow` służącą do zliczania wystąpień słów w tekście. Nowy licznik powinien być pusty.

Klasa ma mieć następujące metody:

- `dodaj_slowo(slowo)` — zwiększa licznik podanego słowa o jeden;
- `liczba_slow(slowo)` — zwraca liczbę wystąpień podanego słowa (zero dla słowa, które nie wystąpiło w tekście);
- `liczba_wszystkich_slow()` — zwraca sumę liczników wszystkich słów;
- `slowa()` — zwraca nową listę zawierającą wszystkie słowa w kolejności ich pierwszego wstawienia.

Napisz również funkcję `wczytaj_licznik(sciezka)`, która:

- odczytuje tekst z pliku;
- dzieli go na słowa za pomocą `str.split()`;
- tworzy i zwraca obiekt `LicznikSlow` zawierający zliczone słowa.

Wielkość liter i znaki interpunkcyjne mają znaczenie, np. `kot`, `Kot` i `kot,` są trzema różnymi słowami.

Napisz program, który przyjmuje ścieżkę pliku tekstowego w wierszu polecenia i wyświetla:

- słowa wraz z liczbą wystąpień, uporządkowane według malejącej częstości, a przy remisie alfabetycznie;
- łączną liczbę wszystkich słów.

**Przykład:** Dla tekstu `kot pies kot Kot` wynik powinien być następujący:

```text
kot: 2
Kot: 1
pies: 1
Łącznie: 4
```

Sprawdź również działanie programu dla pustego pliku (suma powinna wynosić zero).

(cena-podstawowa)=
## 2. Ceny i towary

Napisz klasę `Cena(*, zl=0, gr=0)` reprezentującą kwotę w złotych i groszach.

- Argumenty konstruktora są nieujemnymi liczbami całkowitymi, przekazywanymi wyłącznie przez nazwę.
- Kwotę należy przechowywać jako całkowitą liczbę groszy.
- Wartości podanych argumentów należy normalizować, np. `Cena(zl=2, gr=150)` reprezentuje 3 zł 50 gr.

Zaimplementuj następujące metody:

- `dodaj(inna)` — zwraca nową cenę będącą sumą dwóch cen;
- `roznica(inna)` — zwraca nową cenę będącą wartością bezwzględną różnicy;
- `rowna(inna)` — sprawdza równość dwóch cen;
- `wieksza_od(inna)` — sprawdza, czy cena jest większa od podanej;
- `podnies(procent)` — podnosi cenę o podany procent, zmieniając bieżący obiekt;
- `obniz(procent)` — obniża cenę o podany procent, zmieniając bieżący obiekt;
- `podwyzka(procent)` — zwraca nowy obiekt z podwyższoną ceną, bez zmiany oryginału;
- `obnizka(procent)` — zwraca nowy obiekt z obniżoną ceną, bez zmiany oryginału.

Przy zmianach procentowych obowiązują następujące zasady:

- Procent jest nieujemną liczbą całkowitą.
- Obniżka nie może przekroczyć 100%.
- Wynik zaokrąglamy do pełnego grosza, a dokładną połówkę w górę.
- Obliczenia można wykonać za pomocą arytmetyki całkowitej, bez używania `float`.

Przykładowo podwyżka o 10% ceny 575 gr daje 633 gr.

Zaimplementuj też metody specjalne:

- `__str__` — tekstowa postać ceny, np. `"5 zł 75 gr"`;
- `__repr__` — reprezentacja w postaci wywołania konstruktora, np. `"Cena(zl=5, gr=75)"`.

Napisz klasę `Towar(nazwa, cena)`, która przechowuje nazwę towaru i jego cenę. Konstruktor powinien utworzyć niezależną kopię otrzymanego obiektu `Cena`, tak aby późniejsza zmiana tej ceny nie wpływała na towar.

Napisz następujące funkcje:

- `suma_cen(*ceny)` — zwraca sumę dowolnej liczby cen; dla braku argumentów zwraca cenę zerową;
- `najwyzsza_cena(pierwsza, *pozostale)` — zwraca najwyższą spośród podanych cen;
- `filtruj(towary, *, min_cena=None, max_cena=None, nazwa_zawiera=None)` — zwraca listę towarów spełniających podane warunki.

W funkcji `filtruj`:

- Wszystkie podane warunki muszą być spełnione jednocześnie.
- Granice cen są włączone.
- `nazwa_zawiera` oznacza fragment nazwy towaru.
- Odwrócony zakres cen powoduje zgłoszenie `ValueError`.
- `None` oznacza brak danego ograniczenia.

W funkcjach wykorzystuj metody klasy `Cena`, bez powielania zawartych w nich obliczeń.

Sprawdź czy zmiana ceny jednego towaru nie zmienia ceny innego towaru utworzonego na podstawie tego samego obiektu `Cena`.

Napisz program, który:

1. Odczytuje listę towarów z pliku CSV o kolumnach `nazwa,zl,gr`.
2. Pozwala podnieść lub obniżyć wszystkie ceny o podany procent.
3. Zapisuje zmodyfikowaną listę towarów do nowego pliku CSV.

**Przykładowe dane:**

```csv
nazwa,zl,gr
jabłka,3,60
mąka pszenna,2,80
kawa,25,0
```

Dla tych danych wywołanie `filtruj(towary, min_cena=Cena(zl=5), nazwa_zawiera="ka")` powinno zwrócić listę zawierającą tylko kawę.


(trasy-ulubione)=
## 3. Ulubione trasy

Wykorzystaj klasę `Punkt` z [zestawu 2](../zestaw-02/klasy-obiekty.md). Przyjmij, że współrzędne punktów są wyrażone w metrach, w jednym płaskim układzie współrzędnych.

Napisz klasę `Trasa(nazwa, punkty)` reprezentującą trasę złożoną z kolejnych punktów.

- Trasa przechowuje nazwę i uporządkowaną listę co najmniej dwóch punktów.
- Konstruktor tworzy niezależną kopię otrzymanej listy oraz kopie wszystkich znajdujących się w niej punktów.
- Próba utworzenia trasy z mniej niż dwoma punktami powinna zgłosić `ValueError`.

Zaimplementuj następujące metody:

- `dlugosc()` — zwraca sumę długości odcinków łączących kolejne punkty trasy;
- `przesun(dx, dy)` — przesuwa wszystkie punkty trasy o podany wektor, zmieniając bieżący obiekt;
- `punkty()` — zwraca niezależną kopię listy punktów, zawierającą kopie wszystkich punktów trasy.

Napisz również klasę `Uzytkownik(imie)`, która przechowuje imię użytkownika i listę jego ulubionych tras. Początkowo lista ta jest pusta.

Zaimplementuj metody:

- `dodaj_trase(trasa)` — dodaje trasę do listy ulubionych tras;
- `skopiuj_trasy(inny)` — zastępuje dotychczasową listę ulubionych trasami innego użytkownika.

Zadbaj o niezależność obiektów: zmiana trasy źródłowej lub trasy należącej do jednego użytkownika nie może wpływać na trasy innych użytkowników. Nie używaj listy jako domyślnego argumentu konstruktora.

Napisz funkcje odczytu i zapisu listy tras w formacie JSON. Przykładowa zawartość pliku:

```json
[
  {"nazwa": "Nad rzeką", "punkty": [[0, 0], [300, 0], [300, 400]]},
  {"nazwa": "Do parku", "punkty": [[100, 100], [100, 600]]}
]
```

Do pracy z JSON wykorzystaj moduł `json`, który udostępnia m.in. funkcje:

- `json.load(plik)` — odczytuje dane JSON z otwartego pliku i tworzy odpowiednie obiekty Pythona;
- `json.loads(tekst)` — odczytuje dane JSON z łańcucha znaków;
- `json.dump(dane, plik)` — zapisuje dane Pythona w formacie JSON do otwartego pliku;
- `json.dumps(dane)` — przekształca dane Pythona w łańcuch znaków zawierający JSON.

Napisz program, który:

1. Przyjmuje ścieżkę pliku JSON w wierszu polecenia.
2. Odczytuje listę tras i wyświetla ich nazwy oraz długości.
3. Pozwala użytkownikowi wybrać jedną z tras i podać wektor przesunięcia.
4. Tworzy przesuniętą kopię wybranej trasy i zapisuje ją w nowym pliku JSON, bez modyfikowania trasy źródłowej.

Dla przykładowej trasy „Nad rzeką” długość powinna wynosić 700 m.

Sprawdź również:

- niezależność listy i punktów po utworzeniu obiektu `Trasa`;
- niezależność kopii otrzymanej z metody `punkty()`;
- niezależność tras dwóch użytkowników, również po wykonaniu `skopiuj_trasy`;
- zgłoszenie błędu dla trasy zawierającej tylko jeden punkt.