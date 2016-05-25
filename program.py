import os
import subprocess

print("Podaj nazwe czasteczki: ")
nazwa_czast = input()
nazwa_pliku = nazwa_czast + '.pdb'
czy_zbadany = 0

sc = '/home/szola/Dokumenty/Studia/Bioinformatyka_RNA/Bioinformatyka_Strukturalna/'

if os.path.isfile(sc + '/' + nazwa_czast + '/MC-Ann-' + nazwa_czast):
    czy_zbadany = 0


def u_prog(): # uruchamia programy RNAVIEW i MCAnnotate
    with open(sc + nazwa_czast + "/MC-Ann-" + nazwa_czast, "w") as f:
        subprocess.call([sc + 'MC-Annotate', sc + nazwa_czast + '/' + nazwa_pliku])
    subprocess.run([sc + '/RNAVIEW/bin/rnaview', sc + nazwa_czast + '/' + nazwa_pliku])

    #legenda wynikow:
    #plik "MC-Ann-_" plik wyjsciowy programu MCAnnotate
    #plik "_.pdb.out" plik wyjsciowy programu RNAVIEW
    #pozostale utworzone pliki sa tworzone przez powyzsze programy na roznych etapach ich dzialania


#def u_bd(): #
#    return 0


if czy_zbadany == 0:
    u_prog()
#u_bd()