#Baza oddziaływań wewnątrzcząsteczkowych

Program, który dla danej struktury uzyskuje informacje o klasyfikacji par przez następujące programy zewnętrzne: McAnnotate, RNAView i ClaRNA.
Skrypt bazy danych jest dostępny dla środowiska Oracl, SQLServer i DB2. 

Programy:
McAnnotate – uruchamiany z poziomu pythona, obsługiwany przez program
RNAView - uruchamiany z poziomu pythona, obsługiwany przez program
ClaRNA – uruchamiany tylko on-line, nie obsługiwany przez program

Baza Damych: Skrypt dostępny w SQLServer, Oracl i DB2.

Aby program zadziałał koniecze jest odpowiednie rozmieszczenie plików i folderów. Dla każdej badanej cząsteczki (np. 2n7x.pdb) musi istnieć osobny folder o odpowiedniej nazwie (2n7x) a w nim powinny być dwa pliki: wynik działania programu ClaRna (zapisany w formacie ‘ClaRNA-2n7x.txt’) i plik pdb z badaną cząsteczką (2n7x.pdb).

Program tworzy pliki:  
 - plik "MC-Ann-2n7x" plik wyjsciowy programu MCAnnotate
 - plik "2n7x.pdb.out" albo "2n7x.pdb_nmr.pdb.out" główny plik wyjsciowy programu RNAVIEW
 - pozostałe utworzone pliki są tworzone przez powyższe programy na różnych etapach ich dzialania

#Sposób użycia

Aby program zadziałał konieczne jest skopiowanie ścieżki folderu, w którym będą znajdowały się: folder RNAVIEW i program MC-Annotate.
Rownież koniecze jest odpowiednie rozmieszczenie plików i folderów. Dla każdej badanej cząsteczki (np. 2n7x.pdb) musi istnieć osobny folder (znajdujący się w folderze którego ścieżka została skopiowana do programu) o odpowiedniej nazwie (2n7x) a w nim powinny być dwa pliki: wynik działania programu ClaRna (zapisany w formacie ‘ClaRNA-2n7x.txt’) i plik pdb z badaną cząsteczką (2n7x.pdb).

Wywołanie w terminalu:
```sh
>python program.py
```

#Testy

W folderze Tests zawarte są unittesty które sprawdzają poprawność działania programów. Pliki które chce się przestestować należy umieścić w  folderze Tests.

#Baza
Model relacyjny bazy jest zawarty w repozytorium (Relational.pdf). Zawiera ona 7 tabel, który kolumy są dostosowane do wyników programów MC-Annotate, RNAView i ClaRNA. 
