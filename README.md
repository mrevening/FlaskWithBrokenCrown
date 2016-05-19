======
- Dominik Wieczorek
- Inżynieria Biomedyczna, specjalność: Informatyka i Elektronika Medyczna
- Semestr X
- Projekt realizujący materiał z:
 -**Eksploracja danych i głosowa łączność z komputerem**
- &
- **Asocjacyjne obliczenia w sztucznych systemach skojarzeniowych**

Opis
==============

Projekt zawiera aplikację webową, w której zawarte są materiały do obu projektów, ponieważ materiał
częściowo się pokrywał.

Pliki źródłowe projektu są zamieszczone w repozytorium https://github.com/mrevening/FlaskWithBrokenCrown
W gałęzi *Heroku* znajdują się pliki wrzucone na serwer, więc powinny być najbardziej aktualne.
Applikacja została wrzucona na serwer https://flaskwithbrokencrown.herokuapp.com/result

Dla przedmiotu **Eksploracja danych** z menu głównego aplikacji przeznaczone są:
- Formularz
- Surowe dane
- Wyniki MSBase

Do przedmiotu **Asocjacyjne obliczenia w sztucznych systemach skojarzeniowych** należy zakładka:
- Formularz (do generownia nowych rekordów)
- Graf bazy danych


Wymagania systemowe
==============
- środowisko programistyczne (np. PyCharm Community Edition 2015.1.3)
- python 2.7 (polecany zbiór bibliotek oferowany przez Anaconda - https://www.continuum.io/downloads)
- reszta wymagań znajduje się w pliku requirements.txt

Wykorzystane zasoby (frameworki, biblioteki...)
==============

- Scrapy - przeszukiwanie treści na witrynach internetowych
- Flask - Web Server Gateway Interface
- Sqlite - Baza danych
- Google charts - Tworzenie wykresów


Opis zawartości
==============
Zakładka "Formularz"
--------------

Na tej stronie można uzupełnić formularz. Rodzaj gromadzonych danych pokrywa się z danymi prezentowanymi przez
rejestr MSBase.org Dane gromadzone są w bazie sqlite w pliku formdata.db

Zakładka "Surowe dane"
--------------

Przedstawienie wyników zgromadzonych w formularzu.

Zakładka Wyniki MSBase
--------------
Przedstawia w postaci wykresów (wykorzystane google charts) dane zebrane przy pomocy spidera.

Opis czynności skryptu:
-crawling danych z witryny: https://www.msbase.org/cms/benchmarking.json
    Dane te są pobierane na bieżąco z docelowej witryny, a dane gromadzone w postaci pliku json
    Za te operacje odpowiada moduł *dirbot*
-przekonwertowanie zebranych danych do postaci akceptowalnej przez wykresy google (moduł *unit5*)
-przedstawienie zgromadzonych wyników za pomocą piechart:
    https://developers.google.com/chart/interactive/docs/gallery/piechart

Zakładka "Graf pasywny bazy danych"
--------------

Dla celów projektu z "Asocjacyjne obliczenia w sztucznych systemach skojarzeniowych" powstała grafowa struktura AGDS
pozwalająca uzyskać szybki dostęp do danych.
Za oprawę graficzną odpowiada diagram sankey: https://developers.google.com/chart/interactive/docs/gallery/sankey
Reprezentowane dane pochodzą z wypełnionego formularza.