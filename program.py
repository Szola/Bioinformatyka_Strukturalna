import os
import subprocess

nazwa_czast = input()
nazwa_pliku = nazwa_czast + '.pdb'

sc = '/home/szola/Dokumenty/Studia/Bioinformatyka_RNA/Bioinformatyka_Strukturalna/'

#if not os.path.exists("Wyniki"):
#    os.makedirs("Wyniki")

if not os.path.exists(nazwa_czast):
    os.makedirs(nazwa_czast)
else:
    print("Dana czasteczka zostala juz zbadana!")

with open(sc + nazwa_czast + "/MC-Ann-" + nazwa_czast, "w") as f:
    subprocess.run([sc + 'MC-Annotate', sc + nazwa_czast + '/' + nazwa_pliku])