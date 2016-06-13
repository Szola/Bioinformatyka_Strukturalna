import os
import subprocess

print("Podaj nazwe czasteczki: ")
nazwa_czast = input()
nazwa_pliku = nazwa_czast + '.pdb'
plikPDB = 1

sc = '/home/szola/Dokumenty/Studia/Bioinformatyka_RNA/Bioinformatyka_Strukturalna/'

if os.path.isdir(sc + nazwa_czast):
    plikPDB = 1
else:
    os.mkdir(sc + nazwa_czast)

if os.path.isfile(sc + nazwa_czast + '/' + nazwa_pliku):
    plikPDB = 1
else:
    print("Nie istanieje plik " + nazwa_pliku + " konieczny do zadziałania programu.")
    print("Do folderu " + nazwa_czast + " dodaj plik " + nazwa_pliku + ". Mozna go pobrac ze strony http://www.rcsb.org/pdb/home/home.do")
    plikPDB = 0


def u_prog(): # uruchamia programy RNAVIEW i MCAnnotate
    with open(sc + nazwa_czast + "/MC-Ann-" + nazwa_czast, "w") as f:
        subprocess.call([sc + 'MC-Annotate', sc + nazwa_czast + '/' + nazwa_pliku], stdout=f)
    subprocess.run([sc + '/RNAVIEW/bin/rnaview', sc + nazwa_czast + '/' + nazwa_pliku])


    #legenda wynikow:
    #plik "MC-Ann-_" plik wyjsciowy programu MCAnnotate
    #plik "_.pdb.out" plik wyjsciowy programu RNAVIEW
    #pozostale utworzone pliki sa tworzone przez powyzsze programy na roznych etapach ich dzialania


#def u_bd(): #
#    return 0

if ( plikPDB != 0):
    u_prog()
#u_bd()