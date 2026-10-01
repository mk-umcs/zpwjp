# Temperatury w miastach

## 1. Wyszukiwanie temperatury w liście krotek

Napisz funkcję `znajdz_temperature_w_liscie`, która przyjmuje dwa argumenty:

- `lista_temperatur` &mdash; listę krotek (nazwa miasta, temperatura)
- `nazwa_miasta` &mdash; nazwę miasta do wyszukania

Funkcja zwraca temperaturę dla zadanego miasta. Jeśli miasto nie występuje na liście, funkcja zwraca `None`.

**Przykład użycia:**

```
>>> temperatury = [('Lublin', 23.6), ('Świdnik', 23.5), ('Lubartów', 23.3), ('Łęczna', 23.4)]
>>> znajdz_temperature_w_liscie(temperatury, 'Tokio')  # zwraca None
>>> znajdz_temperature_w_liscie(temperatury, 'Lubartów')
23.3
```

## 2. Wyszukiwanie temperatury w słowniku

Napisz funkcję `znajdz_temperature_w_slowniku`, która przyjmuje dwa argumenty:

- `slownik_temperatur` &mdash; słownik gdzie kluczami są nazwy miast, a wartościami temperatury
- `nazwa_miasta` &mdash; nazwę miasta do wyszukania

Funkcja zwraca temperaturę dla zadanego miasta. Jeśli miasto nie występuje w słowniku, funkcja zwraca `None`.

**Przykład użycia:**

```
>>> temperatury = {'Lublin': 23.6, 'Świdnik': 23.5, 'Lubartów': 23.3, 'Łęczna': 23.4}
>>> znajdz_temperature_w_slowniku(temperatury, 'Nowy Jork')  # zwraca None
>>> znajdz_temperature_w_slowniku(temperatury, 'Łęczna')
23.4
```

## 3. Obliczanie średniej temperatury

Napisz dwie funkcje do obliczania średniej temperatury dla listy miast:

- Funkcja `srednia_temperatura_z_listy`

    - Przyjmuje argument `temperatury` (lista krotek) i `miasta` (lista nazw miast)
    - Zwraca: średnią temperaturę dla podanych miast
    - Zgłasza wyjątek `ValueError` gdy brak danych dla któregoś miasta lub lista miast jest pusta

- Funkcja `srednia_temperatura_ze_slownika`

    - Przyjmuje: `temperatury` (słownik) i `miasta` (lista nazw miast)
    - Zwraca: średnią temperaturę dla podanych miast
    - Zgłasza wyjątek `ValueError` gdy brak danych dla któregoś miasta lub lista miast jest pusta

**Przykład użycia:**
```
>>> temperatury_lista = [('Lublin', 23.6), ('Świdnik', 23.5), ('Lubartów', 23.3), ('Łęczna', 23.4)]
>>> temperatury_slownik = {'Lublin': 23.6, 'Świdnik': 23.5, 'Lubartów': 23.3, 'Łęczna': 23.4}

>>> srednia_temperatura_z_listy(temperatury_lista, ['Lublin', 'Łęczna'])
23.5
>>> srednia_temperatura_ze_slownika(temperatury_slownik, ['Świdnik', 'Lubartów', 'Łęczna'])
23.4

>>> srednia_temperatura_z_listy(temperatury_lista, ['Warszawa'])
Traceback (most recent call last):
    ...
ValueError: brak danych dla miasta 'Warszawa'

>>> srednia_temperatura_ze_slownika(temperatury_slownik, []) 
Traceback (most recent call last):
    ...
ValueError: pusta lista
```

## 4. Parsowanie danych

W pliku tekstowym w każdym wierszu znajduje się nazwa miasta oraz temperatura po spacji. Przykładowy plik z miastami ([`miasta.txt`](miasta.txt), kodowanie to UTF-8) może wyglądać tak: 

```text
Lublin, 23.6
Warszawa, 21.3
Świdnik, 23.5
Rzym, 29.9
Lubartów, 23.3
Łęczna, 23.4
Tokio, 20.1
Londyn, 15.8
Ateny, 34.5
Kraków, 24.1
Szczecin, 17.6
Helsinki, 16.5
Buenos Aires, 9.9
Sydney, 14.4
Nowy Jork, 21.3
```

Napisz funkcję `parsuj_dane_temperaturowe`, która:

- Przyjmuje: `wiersz` &mdash; napis reprezentujący pojedynczy wiersz takiego pliku
- Zwraca: krotkę `(nazwa_miasta, temperatura)` gdzie temperatura jest liczbą zmiennoprzecinkową
- Zgłasza wyjątek `ValueError` w przypadku błędnego formatu (brak przecinka, zbyt wiele przecinków, błędny format liczby)

**Przykład użycia:**

```
>>> parsuj_dane_temperaturowe("Lublin, 23.6")
('Lublin', 23.6)
>>> parsuj_dane_temperaturowe("Warszawa, 21.3")
('Warszawa', 21.3)

>>> parsuj_dane_temperaturowe("Lublin 23.6")
Traceback (most recent call last):
    ...
ValueError: ...

>>> parsuj_dane_temperaturowe("Lublin, 23,6")
Traceback (most recent call last):
    ...
ValueError: ...

>>> parsuj_dane_temperaturowe("Lublin, abc")
Traceback (most recent call last):
    ...
ValueError: ...
```

## 5. Wczytywanie danych z pliku

Napisz dwie funkcje do wczytywania danych temperaturowych z pliku:

- Funkcja `wczytaj_temperatury_do_listy`

    - Przyjmuje: `nazwa_pliku` &mdash; ścieżkę do pliku z danymi
    - Zwraca: listę krotek `[(nazwa_miasta, temperatura), ...]`

- Funkcja `wczytaj_temperatury_do_slownika`

    - Przyjmuje: `nazwa_pliku` &mdash; ścieżkę do pliku z danymi
    - Zwraca: słownik `{nazwa_miasta: temperatura, ...}`

**Przykład użycia:**
```
>>> lista_temp = wczytaj_temperatury_do_listy('miasta.txt')
>>> print(lista_temp)
[('Lublin', 23.6), ('Warszawa', 21.3), ('Świdnik', 23.5), ...]

>>> slownik_temp = wczytaj_temperatury_do_slownika('miasta.txt')
>>> print(slownik_temp)
{'Lublin': 23.6, 'Warszawa': 21.3, 'Świdnik': 23.5, ...}
```

Użyj funkcji z poprzedniego zadania. Podczas wczytywania ignoruj puste wiersze.
Wiersze, które zawierają same białe znaki (spacje, tabulatory, itp., są domyślnie
usuwane przez metodę `str.strip()`) potraktuj
jako puste. 

## 6. Interaktywny program do wyszukiwania temperatur

Napisz program, który:

1. Pyta użytkownika o nazwę pliku z danymi temperaturowymi.
2. Wczytuje dane do słownika.
3. W pętli pyta użytkownika o nazwy miast.
4. Dla każdego miasta wyświetla temperaturę lub komunikat o braku danych.
5. Po wprowadzeniu pustego napisu oblicza i wyświetla średnią temperaturę dla wszystkich miast, o które pytał użytkownik. Średnia jest liczona i wyświetlana tylko jeżeli użytkownik dostał przynajmniej jedą odpowiedź na pytanie o temperaturę. Temperatury mają być wyświetlane z jednym miejscem po przecinku. Miasto jest do średniej liczone raz nawet jeżeli użytkownik pytał o nie wielokrotnie.
6. Program powinien obsługiwać błędy (brak pliku, błędny format danych, itp.)

**Przykłady sesji użytkownika z programem:**
```text
Podaj nazwę pliku z danymi: miasta.txt
Dane wczytane pomyślnie.

Podaj nazwę miasta: Lublin
Temperatura: 23.6°C

Podaj nazwę miasta: Warszawa  
Temperatura: 21.3°C

Podaj nazwę miasta: Tokio
Temperatura: 20.1°C

Podaj nazwę miasta: Paryż
Brak danych

Podaj nazwę miasta: Lublin
Temperatura: 23.6°C

Podaj nazwę miasta:

Średnia temperatura dla podanych miast: 21.7°C
```

```text
Podaj nazwę pliku z danymi: miasta.txt
Dane wczytane pomyślnie.

Podaj nazwę miasta: Rzeszów
Brak danych

Podaj nazwę miasta: Kopenhaga
Brak danych

Podaj nazwę miasta:
```


Dla nieistniejącego pliku:
```text
Podaj nazwę pliku z danymi: nie-ma-takiego-pliku.txt
Nie mogę otworzyć pliku "nie-ma-takiego-pliku.txt".
```

Dla pliku z błędną zawartością, np. takiego jak poniższy plik [`miasta-z-bledami.txt`](miasta-z-bledami.txt) (brak przecinków między nazwą miasta a temperaturą)
```text
Lublin 23.6
Warszawa 21.3
Świdnik 23.5
```
sesja może wyglądać tak:
```text
Podaj nazwę pliku z danymi: miasta-z-bledami.txt
Błędne dane w pliku "miasta-z-bledami.txt"
```

Żeby uzyskać symbol stopnia możesz np. użyć zapisu `'\xb0'`. Na przykład kod `print("15\xb0C")` wyświetli napis `:::text 15°C`.
