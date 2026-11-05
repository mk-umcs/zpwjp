# Polimorfizm i dziedziczenie: ładunki i pracownicy

## 1. Ładunki

Ładunek ma ciężar, wartość, trwałość. Może być delikatny. Zakładamy zatem, że obiekty reprezentujące ładunki muszą mieć następujące metody:

* `ciezar` --- ciężar ładunku (w kilogramach),
* `wartosc` --- wartość ładunku (w groszach),
* `trwalosc` --- trwałość ładunku (w dniach)
* `delikatny` --- czy ładunek jest delikatny

Napisz następujące klasy (różne ładunki) z powyższymi metodami:

### 1.1 Klasa `PlytaCD`

Płyta ma nazwę i cenę (wartości podane w konstruktorze). Każda płyta waży 0.1 kg. Wartość płyty to po prostu jej cena. Trwałość płyty wynosi 10000 dni. Płyta jest ładunkiem delikatnym.

**Przykład użycia:**
```pycon
>>> plyta = PlytaCD('Chopin - Mazurki', 2500)
>>> plyta.ciezar()
0.1
>>> plyta.wartosc()
2500
>>> plyta.trwalosc()
10000
>>> plyta.delikatny()
True
```

### 1.2 Klasa `Jablka`

Jabłka mają odmianę (napis), ilość (w kilogramach), cenę za kilogram i trwałość (w dniach) --- wartości podawane w konstruktorze. Wszystkie parametry poza nazwą są przekazywane jako odpowiednie argumenty nazwane. Wartość jabłek to iloczyn ilości i ceny za kilogram. Jabłka są ładunkiem delikatnym tylko jeżeli odmiana to ,,papierówka''.

**Przykład użycia:**
```pycon
>>> papierowka = Jablka('papierówka', ilosc=5, cena=300, trwalosc=7)
>>> papierowka.ciezar()
5
>>> papierowka.wartosc()
1500
>>> papierowka.trwalosc()
7
>>> papierowka.delikatny()
True

>>> szampion = Jablka('szampion', ilosc=3, cena=400, trwalosc=10)
>>> szampion.delikatny()
False
```

### 1.3. Klasa `Pudelko`

Do pudełka można wkładać różne ładunki (metoda `wloz` dostająca ładunek jako argument). Każde pudełko ma maksymalny ciężar ładunku (wartość podawana w konstruktorze). Próba przeładowania pudełka (włożenie ładunku spowodowałoby przekroczenie maksymalnego ciężaru) powinno skutkować zgłoszeniem wyjątku `ValueError`.

Ciężar pudełka jest sumą ciężarów włożonych do niego ładunków. Podobnie wartość pudełka jest sumą wartości ładunków. Trwałość pudełka to trwałość najmniej trwałego ładunku. Pudełko jest ładunkiem delikatnym jeżeli którykolwiek ładunek włożony do niego jest delikatny.

**Przykład użycia:**
```pycon
>>> pudelko = Pudelko(2.0)
>>> plyta = PlytaCD('Album', 2000)
>>> jablka = Jablka('papierówka', ilosc=1.5, cena=350, trwalosc=5)
>>> pudelko.wloz(plyta)
>>> pudelko.wloz(jablka)
>>> pudelko.ciezar()
1.6
>>> pudelko.wartosc()
2525
>>> pudelko.trwalosc()
5
>>> pudelko.delikatny()
True
```

### Pytania do przemyślenia

Po zaimplementowaniu klas sprawdź następujące rzeczy:

* Czy można włożyć pudełko do innego pudełka (powinno się dać)?
* Czy da się włożyć pudełko do samego siebie (nie powinno się dać, jak wykryć próbę wykonania takiej operacji)? Jeżeli to działa, to sprawdź np. czy da się teraz sprawdzić jaka jest wartość tego pudełka.
* Czy można ten sam obiekt włożyć równocześnie do wielu pudełek? Nie powinno się dać, ale wykrycie tego wymaga albo przechowywania przez każdy ładunek dodatkowej informacji o tym, czy jest już zapakowany do jakiegoś pudełka (rozważ wykorzystanie dziedziczenia do implementacji tego) lub przechowywania gdzieś osobno informacji o wszystkich spakowanych już gdzieś ładunkach.

### 1.4. Metoda `zawiera`

Dodaj metodę `zawiera(ladunek)` sprawdzającą, czy dokładnie ten obiekt jest bezpośrednio włożony do pudełka. Sprawdzamy tożsamość obiektu, a nie podobieństwo jego danych. Metoda nie przeszukuje zawartości wewnętrznych pudełek.

```pycon
>>> pudelko = Pudelko(1.2)
>>> plyta = PlytaCD('Chopin - Mazurki', 20)
>>> pudelko.wloz(plyta)
>>> pudelko.zawiera(plyta)
True
>>> druga_plyta = PlytaCD('Chopin - Mazurki', 20)
>>> pudelko.zawiera(druga_plyta)
False
```

### 1.5. Implementacja operatora `in`

Metoda specjalna `__contains__` odpowiada za operator `in`, tzn. wyrażenie `x in p` ma wartość taką jak `bool(p.__contains__(x))`. Napisz odpowiednią implementację tej metody działającą tak jak w kodzie poniżej:

```pycon
>>> pudelko = Pudelko(1.2)
>>> plyta = PlytaCD('Chopin - Mazurki', 20)
>>> pudelko.wloz(plyta)
>>> plyta in pudelko
True
```


Obie wersje operacji mają dawać ten sam wynik. W implementacji operatora wykorzystaj metodę `zawiera`, aby nie powielać sprawdzania.

### 1.6. Program wykorzystujący ładunki

Napisz [program do przygotowania przesyłki](ladunki-program.md). Kolejne etapy prowadzą od raportu dla prostych pudełek przez zagnieżdżenia i wykrywanie błędów do opcjonalnych napraw.


## 2. Pracownicy

### 2.1. Klasa `Osoba`

Napisz klasę `Osoba`. Osoba ma imię i nazwisko.

**Przykład użycia**

```pycon
>>> osoba = Osoba('Jan', 'Kowalski')
>>> osoba.imie
'Jan'
>>> osoba.nazwisko
'Kowalski'
>>> osoba.imie = 'Adam'
>>> print(f"{osoba.imie} {osoba.nazwisko}")
Adam Kowalski
```

### 2.2. Klasa `Pracownik`

Napisz klasę `Pracownik`. Pracownik ma imię i nazwisko, ale ma też miesięczną pensję (liczba całkowita w pełnych złotych zadana w konstruktorze). Klasa ma mieć metodę `roczne_zarobki` zwracającą roczne zarobki pracownika (12 miesięcznych pensji).

**Przykład użycia:**

```pycon
>>> pracownik = Pracownik('Anna', 'Wiśniewska', 5000)
>>> pracownik.imie
'Anna'
>>> pracownik.nazwisko
'Wiśniewska'
>>> pracownik.pensja
5000
>>> pracownik.roczne_zarobki()
60000
```

### 2.3. Klasa `PrzedstawicielHandlowy`

Napisz klasę `PrzedstawicielHandlowy`. Przedstawiciel handlowy jest pracownikiem, który oprócz pensji dostaje prowizję od sprzedanego towaru. Prowizja jest obliczana jako procent wartości całego sprzedanego przez przedstawiciela towaru. Wartość procentowa (zawsze całkowita) jest przekazana w konstruktorze argumentem nazwanym (ma to być wymuszone) `prowizja`. Oprócz metod z klasy `Pracownik` klasa `PrzedstawicielHandlowy` ma metodę `sprzedaj_towar`. Sprzedaż towaru przez przedstawiciela oznacza wywołanie tej metody z argumentem oznaczającym wartość towaru. Prowizja (procent wartości sprzedanego towaru zaokrąglony w dół do liczby całkowitej) powinien być uwzględniony przy obliczaniu rocznych zarobków.

**Przykład użycia**

W przykładzie przedstawiciel zarabia miesięcznie 3000 zł (12 × 3000 = 36000) i sprzedał łącznie towar za 1100 zł z czego 55 zł jest jego zarobkiem (0.05 × 1100 = 55). Jego roczne zarobki zatem to 36055 zł.

```pycon
>>> przedstawiciel = PrzedstawicielHandlowy('Adam', 'Nowakowski', 3000, prowizja=5)
>>> przedstawiciel.imie
'Adam'
>>> przedstawiciel.pensja
3000
>>> przedstawiciel.sprzedaj_towar(1000)
>>> przedstawiciel.sprzedaj_towar(100)
>>> przedstawiciel.roczne_zarobki()
36055
```

### 2.4. Klasa `Menedzer`

Napisz klasę `Menedzer`. Menedżer jest zatrudniony na rocznym kontrakcie i nie ma w ogóle ustalonej miesięcznej pensji. Wartość kontraktu jest przekazywana w konstruktorze jako argument nazwany `wartosc_kontraktu`. 

**Przykład użycia:**

```pycon
>>> menedzer = Menedzer('Tomasz', 'Lewandowski', wartosc_kontraktu=120000)
>>> menedzer.imie
'Tomasz'
>>> menedzer.nazwisko
'Lewandowski'
>>> menedzer.roczne_zarobki()
120000
```

### 2.5. Funkcja `suma_rocznych_zarobkow`

Napisz funkcję `suma_rocznych_zarobkow`, która dla zadanej sekwencji pracowników zwraca sumę rocznych zarobków wszystkich pracowników z sekwencji.

**Przykład użycia:**

W poniższym przykładzie suma rocznych zarobków to 60000 (pracownik) + 36055 (przedstawiciel handlowy) + 120000 (menedżer) + 48000 (pracownik) = 264055.

```pycon
>>> anna = Pracownik('Anna', 'Wiśniewska', 5000)
>>> adam = PrzedstawicielHandlowy('Adam', 'Nowakowski', 3000, prowizja=5)
>>> adam.sprzedaj_towar(1100)
>>> tomasz = Menedzer('Tomasz', 'Lewandowski', wartosc_kontraktu=120000)
>>> jan = Pracownik('Jan', 'Kowalski', 4000)
>>> pracownicy = [anna, adam, tomasz, jan]
>>> suma_rocznych_zarobkow(pracownicy)
264055
```

Jakiego typu obiekty mogą być w zadanej sekwencji? Sprawdź (np. wykonując kod poniżej) co się stanie jeżeli w sekwencji znajdzie się obiekt typu `Osoba`.

```pycon
>>> osoba = Osoba('Jan', 'Kowalski')
>>> pracownik = Pracownik('Anna', 'Wiśniewska', 5000)
>>> suma_rocznych_zarobkow([osoba, pracownik])
```


### 2.6. Program

Używając klas z poprzednich zadań napisz program wczytujący z pliku tekstowego dane o pracownikach. W każdym wierszu są informacje o jednym pracowniku.

Pierwszy znak w wierszu oznacza stanowisko pracownika. Znak `p` oznacza przedstawiciela handlowego, a `m` menedżera. Jeżeli nie jest znane stanowisko, to pierwszym znakiem jest znak `-`.

Po pierwszym znaku jest spacja oraz wiek pracownika. W tym programie wczytaj wiek, ale nie wykorzystuj go przy tworzeniu obiektów: klasy z punktów 2.1–2.4 przechowują imię i nazwisko, a nie wiek. Po wieku jest kolejna spacja oraz imię i nazwisko (również oddzielone spacją).

Jeżeli pracownik jest menedżerem, to po kolejnej spacji występuje wartość jego kontraktu.

Dla innych pracowników kolejnym elementem wiersza jest pensja. 

W przypadku przedstawiciela handlowego w wierszu są jeszcze kolejne oddzielone spacjami liczby całkowite. Pierwsza z nich oznacza procent od wartości sprzedanego towaru, a kolejne wartości kolejnych sprzedanych towarów.

Przykładowy plik może wyglądać tak:

```
p 25 Fryderyk Brzeziński 300000 5 100000 200000 300000
- 30 Halina Górska 500000
m 35 Kinga Pawlak 10000000
- 40 Krystian Krawczyk 400000
```

Program w pliku wynikowym zapisuje dla każdego pracownika jego imię nazwisko oraz roczne zarobki. W ostatnim wierszu pliku zapisywana jest suma rocznych zarobków wszystkich pracowników.

Np. dla przykładowego pliku wejściowego plik wynikowy wyglądałby tak:

```
Fryderyk Brzeziński 3630000
Halina Górska 6000000
Kinga Pawlak 10000000
Krystian Krawczyk 4800000
24430000
```
