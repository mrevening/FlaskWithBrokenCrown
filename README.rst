======
Dominik Wieczorek
Inżynieria Biomedyczna
Semestr X
Projekt na przedmioty:
Eksploracja danych i głosowa łączność z komputerem
&
Asocjacyjne obliczenia w sztucznych systemach skojarzeniowych

Opis
======

Projekt zawiera aplikację webową.
--Zakładka Wyniki MSBase--
Umożliwia:
-crawling danych z witryny: https://www.msbase.org/cms/benchmarking.json
-przedstawienie zgromadzonych wyników za pomocą piechart: https://developers.google.com/chart/interactive/docs/gallery/piechart
-uzupełnienie formularza i wyświetlenie zebranych rekordów
-przedstawienie wyników formularza za pomocą pasywnych grafowych struktur skojarzeniowych

Projek wykorzystywany tylko do celów edukacyjnych


Wykorzystane zasoby
=====

-Scrapy - przeszukiwanie treści na witrynach internetowych
-Flask - Web Server Gateway Interface
-Sqlite - Baza danych
-Google charts - Tworzenie wykresów

The items scraped by this project are websites, and the item is defined in the
class::

    dirbot.items.Website

See the source code for more details.

Zakładka "Wyniki MSBase"
=======

Umożliwia crawling danych z witryny: https://www.msbase.org/cms/benchmarking.json
i przedstawienie wyników za pomocą piechart: https://developers.google.com/chart/interactive/docs/gallery/piechart

Ta witryna może ładować się dłużej niż pozostałe.

Spider: crawlmycrown.py
------------
W folderze dirbot/spiders znajduje się spider który pobiera informacje zawarte między znacznikami html
z ogólnie dostępnego projektu MSBase (https://www.msbase.org/cms/benchmarking.json).
W tym przypadku są to statystyki użytkowników tego rejestru chorych na stwardnienie rozsiane.

Zakładka "Formularz"
=========

Na tej stronie można uzupełnić formularz, którego wyniki są identyczne z wynikami przedstawianymi
przez rejestr MSBase.org . Dane gromadzone są w bazie formdata.db

Zakładka "Surowe dane"
=========

Przedstawienie wyników zgromadzonych w formularzu.

Zakładka "Graf pasywny bazy danych"
=========


