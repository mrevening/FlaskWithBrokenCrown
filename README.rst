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

Zakładka "Formularz"
=========

Na tej stronie można uzupełnić formularz, którego wyniki są identyczne z wynikami przedstawianymi
przez rejestr MSBase.org . Dane gromadzone są w bazie formdata.db

Zakładka "Surowe dane"
=========

Przedstawienie wyników zgromadzonych w formularzu.

Zakładka "Wyniki MSBase"
=======

Umożliwia crawling danych z witryny: https://www.msbase.org/cms/benchmarking.json
i przedstawienie wyników za pomocą piechart: https://developers.google.com/chart/interactive/docs/gallery/piechart

Ta witryna może ładować się dłużej niż pozostałe.

Zakładka "Graf pasywny bazy danych"
=========

Dla celów projektu z "Asocjacyjne obliczenia w sztucznych systemach skojarzeniowych" powstała grafowa struktura AGDS
pozwalająca uzyskać szybki dostęp do danych.
Za oprawę graficzną odpowiada diagram sankey: https://developers.google.com/chart/interactive/docs/gallery/sankey
Reprezentowane są dane z wypełnionego formularza.
