# Ładunki — program do przygotowania przesyłki

Wykorzystaj klasy `PlytaCD`, `Jablka` i `Pudelko` z [zadania o ładunkach](ladunki-pracownicy.md). Program ma pomóc sprawdzić przesyłkę przed wysłaniem i przygotować raport o jej paczkach. Paczką nazywamy pudełko, które nie znajduje się w żadnym innym pudełku. Przesyłka może składać się z wielu paczek.

Kolejne etapy rozbudowują ten sam program. Po etapie 1 działa raport dla prostych danych, po etapie 2 także dla poprawnie zagnieżdżonych pudełek. Etapy 3–4 dodają kontrolę danych, a etap 5 — możliwość naprawy wybranych błędów.

## 1. Raport dla prostych pudełek

### Dane wejściowe

Do odczytu pliku użyj modułu `json` i funkcji `json.load`. Plik JSON zawiera listę opisów obiektów. Każdy opis ma niepusty napis `id` identyfikujący konkretny egzemplarz oraz pole `typ`:

| Typ | Pozostałe pola | Tworzony obiekt |
| --- | --- | --- |
| `plyta` | `nazwa`, `cena` | `PlytaCD(nazwa, cena)` |
| `jablka` | `odmiana`, `ilosc`, `cena`, `trwalosc` | `Jablka(odmiana, ilosc=ilosc, cena=cena, trwalosc=trwalosc)` |
| `pudelko` | `maks_ciezar`, `zawartosc` | `Pudelko(maks_ciezar)`, do którego wkładamy wskazane obiekty |

`cena` oznacza grosze: cenę płyty albo cenę kilograma jabłek. `ilosc` i `maks_ciezar` są wyrażone w kilogramach, a `trwalosc` w dniach. `zawartosc` jest listą identyfikatorów bezpośrednio włożonych ładunków. Inny identyfikator oznacza inny egzemplarz, nawet jeżeli obie płyty mają tę samą nazwę i cenę.

Przykładowy plik [proste.json](ladunki-dane/proste.json):

```{literalinclude} ladunki-dane/proste.json
:language: json
```

W tym etapie możesz założyć, że dane są poprawne: wszystkie towary są w pudełkach, pudełka zawierają tylko płyty lub jabłka, nie są puste ani przeciążone, a każdy obiekt znajduje się najwyżej w jednym pudełku.

### Zadanie

1. Wczytaj opisy i utwórz obiekty odpowiednich klas. Przechowuj je w słowniku według identyfikatorów. Jeden opis tworzy jeden obiekt.
2. Włóż towary do pudełek, korzystając z tych samych obiektów, które znajdują się w słowniku. Nie twórz kopii towaru przy każdym odwołaniu do jego identyfikatora.
3. Zapisz liczbę paczek i dla każdej paczki cztery informacje: ciężar, wartość, trwałość i delikatność. Wywołuj wspólny interfejs ładunków; program nie powinien ponownie implementować reguł liczenia ciężaru lub wartości jabłek i płyt.

Program przyjmuje nazwę pliku wejściowego i raportu, np.:

```text
python ladunki.py ladunki-dane/proste.json raport.txt
```

Raport uporządkuj według identyfikatorów paczek. Dla powyższych danych oczekiwany [raport](ladunki-dane/proste-raport.txt) wygląda tak:

```{literalinclude} ladunki-dane/proste-raport.txt
:language: text
```

Oddziel odczyt danych, tworzenie obiektów, obliczenie informacji o przesyłce i zapis raportu. Nie umieszczaj obsługi plików w klasach ładunków.

## 2. Pudełka w innych pudełkach

Rozszerz program na pudełka zawierające także inne pudełka. Format pliku pozostaje taki sam. Nie zakładaj, że opis ładunku występuje przed opisem pudełka, które się do niego odwołuje.

Najpierw utwórz wszystkie obiekty, a potem zbuduj powiązania. Przy wkładaniu możesz potrzebować zacząć od pudełek najbardziej wewnętrznych: ciężar zawartości musi być już znany, aby sprawdzić pojemność pudełka. Przykładowe dane na tym etapie nadal są poprawne i nie zawierają cykli.

Raport obejmuje wyłącznie pudełka zewnętrzne. Nie dopisuj osobno ich wewnętrznych pudełek i nie licz drugi raz zawartości przesyłki.

W [zagniezdzone.json](ladunki-dane/zagniezdzone.json) obiekt `b0` ma zawartość `["b1", "b2"]` i limit 5 kg. Reszta to te same towary i pudełka co poprzednio. Oczekiwany [raport](ladunki-dane/zagniezdzone-raport.txt):

```{literalinclude} ladunki-dane/zagniezdzone-raport.txt
:language: text
```

Dla pustej listy opisów ([pusta-przesylka.json](ladunki-dane/pusta-przesylka.json)) raport ma zawierać `Liczba paczek: 0`.

## 3. Kontrola opisów i powiązań

Znieś założenie o poprawności wejścia. Zanim zaczniesz wkładać ładunki do pudełek i obliczać ich parametry, sprawdź:

- poprawność JSON, wymaganych pól i ich typów;
- niepuste, unikalne identyfikatory i rozpoznawane typy ładunków;
- nieujemne całkowite ceny i trwałość, dodatnią ilość jabłek i dodatni limit ciężaru;
- istnienie wszystkich identyfikatorów wymienionych w zawartości;
- czy ten sam identyfikator nie jest wymieniony dwa razy w jednym pudełku;
- czy jeden obiekt nie znajduje się bezpośrednio w kilku pudełkach;
- czy pudełko nie zawiera siebie samego i czy nie ma dłuższego cyklu, np. `a → b → c → a`.

Liczby zmiennoprzecinkowe w danych muszą być skończone. Identyfikatory sprawdzaj niezależnie od kolejności rekordów. Cykli szukaj w całym zbiorze opisów, a nie tylko od znalezionych paczek: w cyklu mogą w ogóle nie istnieć pudełka zewnętrzne.

Przy badaniu cykli przydaje się zapamiętanie bieżącej ścieżki przechodzenia przez powiązania. Nie dopuszczaj do uruchomienia nieskończonej rekurencji w `ciezar()`, `wartosc()` lub `zawiera`.

Przykłady do sprawdzenia:

| Plik | Co powinien wykryć program |
| --- | --- |
| [nieznany-id.json](ladunki-dane/nieznany-id.json) | pudełko `a` wskazuje brakujący obiekt |
| [powtorzony-id.json](ladunki-dane/powtorzony-id.json) | dwa opisy mają identyfikator `p1` |
| [powtorzony-wpis.json](ladunki-dane/powtorzony-wpis.json) | `p1` występuje dwukrotnie w `a` |
| [wspolny-towar.json](ladunki-dane/wspolny-towar.json) | tę samą płytę przypisano do dwóch pudełek |
| [wiele-pudelek.json](ladunki-dane/wiele-pudelek.json) | to samo pudełko `wew` przypisano do `a` i `b` |
| [samo-w-sobie.json](ladunki-dane/samo-w-sobie.json) | pudełko `a` zawiera samo siebie |
| [cykl.json](ladunki-dane/cykl.json) | cykl `a → b → a` bez pudełka zewnętrznego |

Komunikat ma wskazywać rodzaj problemu i identyfikatory obiektów, których dotyczy. Po wykryciu błędu nie twórz raportu wyglądającego jak raport poprawnej przesyłki.

## 4. Czy przesyłka nadaje się do wysłania?

Dla strukturalnie poprawnych danych sprawdź jeszcze reguły pakowania:

1. Każdy towar znajduje się w pudełku — nie wysyłamy luźnej płyty ani luźnych jabłek.
2. Żadne pudełko, również wewnętrzne, nie jest puste.
3. Pudełko nie zawiera wyłącznie jednego innego pudełka. W tym modelu opakowanie nie zwiększa ciężaru ani wartości i nie zmienia trwałości, więc takie dodatkowe opakowanie uznajemy za zbędne.
4. Żaden limit ciężaru nie jest przekroczony, także w pudełkach wewnętrznych.

Nie dodawaj współczynnika ciężaru samego opakowania — używamy definicji klasy z poprzedniej części zadania. [przeciazenie.json](ladunki-dane/przeciazenie.json) pokazuje płytę o ciężarze 0,1 kg w pudełku o limicie 0,05 kg.

Nie wystarczy sprawdzić limitu tylko podczas pierwszego `wloz`. Jeżeli najpierw zapakujesz puste pudełko wewnętrzne, a potem dodasz do niego towary, ciężar pudełka zewnętrznego również wzrośnie. Sprawdź końcowy stan całej przesyłki przed zapisaniem raportu.

Po błędzie nie nadpisuj wcześniej istniejącego raportu. Program ma podać przyczynę, a dane wejściowe mają pozostać bez zmian.

## 5. Opcjonalne naprawy

Dodaj tryb `--napraw`. Naprawy wykonuj dopiero po potwierdzeniu poprawności opisów i powiązań z etapu 3 oraz limitów ciężaru. Program nie ma samodzielnie zgadywać rozwiązania cyklu, wielokrotnego przypisania, nieznanego identyfikatora ani sposobu przepakowania przeciążenia.

Dla pozostałych błędów wykonaj następujące operacje:

- Usuń wszystkie puste pudełka, także odwołania do nich z zawartości rodziców.
- Jeżeli pudełko zawiera wyłącznie jedno inne pudełko, usuń zewnętrzne opakowanie, a jego wystąpienie u rodzica zastąp wewnętrznym pudełkiem. Jeżeli usuwasz paczkę zewnętrzną, jej zawartość staje się paczką.
- Powtarzaj te kroki, dopóki nie ma kolejnych pustych lub zbędnych pudełek.
- Wszystkie pozostałe luźne towary zapakuj razem do jednego nowego pudełka. Nadaj mu pierwszy wolny identyfikator `nowe_1`, `nowe_2` itd. Limit dobierz jako sumę ciężarów jego zawartości. Jeżeli nie ma luźnych towarów, nie twórz nowego pudełka.

Po naprawach ponownie sprawdź wszystkie reguły. Zapisz naprawione opisy do osobnego pliku JSON, a raport utwórz na ich podstawie. Nie zmieniaj oryginalnego pliku i nie kopiuj samych towarów. Wyświetl również listę wykonanych napraw z identyfikatorami usuniętych i dodanych pudełek.

Przykładowe wywołanie:

```text
python ladunki.py --napraw ladunki-dane/do-naprawy.json naprawione.json raport.txt
```

Plik [do-naprawy.json](ladunki-dane/do-naprawy.json) zawiera luźną płytę `p1`, puste pudełko `puste` i zbędne opakowanie `zew` zawierające tylko `wew`. Bez trybu naprawy program powinien wskazać te problemy.

Po naprawie pozostają `wew` z jabłkami i nowe pudełko `nowe_1` z płytą. Porównaj wynik ze [spodziewanymi opisami](ladunki-dane/po-naprawie.json) i [raportem](ladunki-dane/po-naprawie-raport.txt). Kolejność opisów obiektów w JSON nie ma znaczenia; kolejność wierszy raportu nadal wynika z identyfikatorów paczek.

## Sprawdzenie programu

- Po zamianie kolejności opisów wynik pozostaje ten sam.
- Wszystkie załączone poprawne przykłady dają podane raporty.
- Niepoprawne struktury są wykrywane przed wywołaniem rekurencyjnych obliczeń.
- Ten sam egzemplarz nie jest kopiowany przy budowie powiązań; dwa różne identyfikatory mogą opisywać dwa podobne towary.
- Zmiana zawartości wewnętrznego pudełka wpływa na parametry zewnętrznego.
- Naprawa nie zmienia oryginału, nie gubi towarów i nie tworzy ich kopii.
- Ponowne uruchomienie naprawy na poprawionym pliku niczego już nie zmienia.

