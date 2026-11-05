# Ceny, towary i filtry — argumenty nazwane oraz kopie

Klasy w tym zestawie wykorzystują publiczne pola. W części podstawowej nie używaj właściwości ani operatorów poza `__str__` i `__repr__`. Grosze są tutaj normalizowane, inaczej niż w wariancie z walidacją zakresu 0–99.

## Klasa `Cena`

Napisz klasę `Cena` reprezentującą cenę w złotych i groszach.

**Wymagania**:

- Konstruktor musi przyjmować argumenty nazwane: `zl` i `gr`
- Grosze powinny być automatycznie normalizowane (np. 150 gr = 1 zł 50 gr)

**Metody do zaimplementowania**:

- odpowiednie metody konwertujące obiekt na napis (patrz przykłady użycia)
- `dodajCene(self, inna_cena)` --- przyjmuje drugi obiekt klasy `Cena`, zwraca nowy obiekt będący sumą cen
- `roznicaCen(self, inna_cena)` --- zwraca dodatnią różnicę między cenami (kolejność nie ma znaczenia)
- `wiekszaOd(self, inna_cena)` --- zwraca `True` jeśli cena jest większa od podanej
- `rowne(self, inna_cena)` --- zwraca `True` jeśli ceny są równe
- `podnies(self, procent)` --- podnosi cenę o podany procent (liczba dodatnia), modyfikuje obiekt, zaokrągla do pełnych groszy
- `obniz(self, procent)` --- obniża cenę o podany procent (liczba dodatnia), modyfikuje obiekt, zaokrągla do pełnych groszy
- `podwyzka(self, procent)` --- zwraca nowy obiekt z podniesioną ceną o podany procent
- `obnizka(self, procent)` --- zwraca nowy obiekt z obniżoną ceną o podany procent

*Wskazówka:* metody `podwyzka` i `obnizka` mogą wykorzystywać użycie metod `podnies` i `obniz` na kopii obiektu, metody mające parametr `procent` powinny zgłaszać wyjątek `ValueError` jeżeli procent nie jest dodatni.

### Przykłady użycia:

```pycon
>>> c1 = Cena(zl=10, gr=50)
>>> repr(c1)
'Cena(zl=10, gr=50)'
>>> c1
Cena(zl=10, gr=50)

>>> c2 = Cena(zl=5, gr=75)
>>> suma = c1.dodajCene(c2)
>>> print(suma)
16 zł i 25 gr

>>> roznica = c1.roznicaCen(c2)
>>> print(roznica)
4 zł i 75 gr

>>> c1.wiekszaOd(c2)
True

>>> c1.podnies(10)
>>> print(c1)
11 zł i 55 gr

>>> c3 = c2.obnizka(20)
>>> print(c2)  # oryginał niezmieniony
5 zł i 75 gr
>>> print(c3)  # nowy obiekt
4 zł i 60 gr

>>> Cena(3, 50)
Traceback (most recent call last):
...
TypeError: Cena.__init__() takes 1 positional argument but 3 were given
```

## Funkcje operujące na cenach

Napisz następujące funkcje:

- `sumaCen` --- przyjmuje dowolną liczbę obiektów `Cena`, zwraca ich sumę,
- `najwyzszaCena` --- przyjmuje jeden lub więcej obiekt `Cena`, zwraca najwyższą cenę z podanych,
- `najnizszaCena` --- przyjmuje jeden lub więcej obiekt `Cena`, zwraca najniższą cenę z podanych.


### Przykłady użycia:
```pycon
>>> sumaCen(Cena(zl=1,gr=0), Cena(zl=2,gr=50), Cena(zl=3,gr=75))
Cena(zl=7, gr=25)

>>> ceny = [Cena(zl=1,gr=0), Cena(zl=2,gr=50), Cena(zl=3,gr=75)]
>>> suma = sumaCen(*ceny)
>>> suma
Cena(zl=7, gr=25)
>>> sumaCen()
Cena(zl=0, gr=0)

>>> najwyzszaCena(*ceny)
Cena(zl=3, gr=75)
>>> najnizszaCena(*ceny)
Cena(zl=1, gr=0)

>>> najwyzszaCena()
Traceback (most recent call last):
...
TypeError: najwyzszaCena() missing 1 required positional argument: ...

```

## Klasa `Towar`

Napisz klasę `Towar` reprezentującą towar z nazwą i ceną (pola `nazwa` i `cena`).

**Metody do zaimplementowania**:

- `__str__(self)` --- zwraca napis w postaci: `"jabłka: 5 zł i 80 gr"`
- `__repr__(self)` --- zwraca napis w postaci: `"Towar('gruszki', Cena(zl=4, gr=50))"`
- `podniesCene(self, procent)` --- podnosi cenę towaru o podany procent
- `obnizCene(self, procent)` --- obniża cenę towaru o podany procent

*Wskazówka*: wykorzystaj metody z klasy `Cena`.

### Przykłady użycia:
```pycon
>>> jablka = Towar("jabłka", Cena(zl=5, gr=80))
>>> print(jablka)
jabłka: 5 zł i 80 gr
>>> jablka.podniesCene(10)
>>> print(jablka)
jabłka: 6 zł i 38 gr
>>> gruszki = Towar("gruszki", Cena(zl=4, gr=50))
>>> repr(gruszki)
"Towar('gruszki', Cena(zl=4, gr=50))"
```

### Pytanie dodatkowe

Czy obiekt `Towar` powinien tworzyć kopię ceny otrzymanej jako argument? Jeżeli nie, to co będzie w poniższym przypadku:

```pycon
>>> cena = Cena(zl=3, gr=60)
>>> jablka = Towar("jabłka", cena)
>>> gruszki = Towar("gruszki", cena)
>>> jablka.cena.podnies(10)
>>> print(gruszki.cena)
```

## Funkcja filtruj

Napisz funkcję `filtruj` która przyjmuje sekwencję towarów i zwraca listę pasujących towarów. Funkcja musi mieć możliwość zastosowania następujących filtrów (wszystkie jako argumenty nazwane):

- `min_cena` --- minimalna cena towaru (obiekt klasy Cena), towary z ceną niższą są odrzucane,
- `max_cena` --- maksymalna cena towaru (obiekt klasy Cena), towary z ceną wyższą są odrzucane,  
- `nazwa_zawiera` --- napis, który musi być zawarty w nazwie towaru (wielkość liter ma znaczenie).

Nie wszystkie filtry muszą być użyte w danym wywołaniu. Jeśli filtr nie jest podany, nie wpływa na wynik.

### Przykład użycia:

Załóżmy, że mamy następujące towary:

```pycon
>>> t1 = Towar("jabłka", Cena(zl=3, gr=50))
>>> t2 = Towar("jabłka żółte", Cena(zl=4, gr=20))
>>> t3 = Towar("gruszki", Cena(zl=2, gr=80))
>>> t4 = Towar("czerwone jabłka", Cena(zl=5, gr=10))
```

Wywołanie będzie działać następująco:
```pycon
>>> wynik = filtruj([t1, t2, t3, t4], max_cena=Cena(zl=4, gr=50), nazwa_zawiera="jab")
[Towar('jabłka', Cena(zl=3, gr=50)), Towar("jabłka żółte", Cena(zl=4, gr=20))]
```

Działanie filtrów:

- Filtr `max_cena=Cena(zl=4, gr=50)` zwróci towary: `t1`, `t2`, `t3` (cena ≤ 4,5 zł)
- Filtr `nazwa_zawiera="jab"` zwróci towary: `t1`, `t2`, `t4` (nazwa zawiera `"jab"`)

Wynik końcowy (przecięcie filtrów) `t1` i `t2`


## Konwersja cen netto na brutto

Plik wejściowy w kodowaniu UTF-8 zawiera w każdym wierszu nazwę cenę i stawkę VAT w następującym formacie:

```text
nazwa;cena_zl;cena_gr;stawka_VAT
```

Przykładowy plik `towary_netto.txt`:
```text
jabłka;3;60;5
mąka pszenna;2;80;8
ser żółty;12;50;23
chleb;4;20;5
woda mineralna;1;50;8
sok pomarańczowy;5;90;23
cukier;3;20;8
herbata;8;40;5
kawa;25;00;23
masło;6;70;8
```

Napisz program, który powinien:

1. Pytać użytkownika o nazwę pliku wejściowego i wyjściowego
2. Generować odpowiedni plik wyjściowy z wierszami w formacie: 
   
   ```text
   nazwa;cena_brutto_zl;cena_brutto_gr
   ```

Przykładowy plik wynikowy `towary_brutto.txt`:
```text
jabłka;3;78
mąka pszenna;3;2
ser żółty;15;38
chleb;4;41
woda mineralna;1;62
sok pomarańczowy;7;26
cukier;3;46
herbata;8;82
kawa;30;75
masło;7;24
```

## Interaktywne filtrowanie towarów

Program powinien:

1. Wczytać towary z pliku w formacie brutto
2. Pytać użytkownika o filtry:
   - czy filtrować po nazwie? (tak/nie), jeżeli tak, to o wartość filtra
   - czy filtrować po minimalnej cenie? (tak/nie) i ewentualnie o minimalną cenę.
   - czy filtrować po maksymalnej cenie? (tak/nie) i ewentualnie o maksymalną cenę.
3. Zapisać wyniki do nowego pliku

### Przykład sesji z użytkownikiem

```text
Podaj nazwę pliku z towarami: towary_brutto.txt

Czy chcesz filtrować po nazwie? (t/n): t
Podaj fragment nazwy: ka
Czy chcesz filtrować po minimalnej cenie? (t/n): t
Podaj minimalną cenę (w zł): 5.00
Czy chcesz filtrować po maksymalnej cenie? (t/n): n

Znaleziono 1 towar:
- kawa: 30 zł i 75 gr

Podaj nazwę pliku wynikowego: przefiltrowane.txt
```

Plik wynikowy `przefiltrowane.txt`:
```text
kawa;30;75
```
