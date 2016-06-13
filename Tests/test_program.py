import unittest
from os import getcwd, remove, listdir
from os.path import sep, isfile
import subprocess


class ProgramTests(unittest.TestCase):
    def setUp(self):
        self.sc = '/home/szola/Dokumenty/Studia/Bioinformatyka_RNA/Bioinformatyka_Strukturalna/'


    def test_mc_annotate(self):
        nazwa_czast = "2n7x"
        sc_pliku_wej = getcwd() + sep + nazwa_czast + ".pdb"
        sc_pliku_wyj = getcwd() + sep + "MC-Ann-" + nazwa_czast
        with open(sc_pliku_wyj, "w") as f:
            subprocess.call([self.sc + 'MC-Annotate', sc_pliku_wej], stdout=f)

        self.assertTrue(isfile(sc_pliku_wyj))

        with open(sc_pliku_wyj, "r") as f:
            lines = f.read()
            self.assertTrue(lines)

        remove(sc_pliku_wyj)


    def test_rnaview(self):
        nazwa_czast = "2n7x"
        sc_pliku = getcwd() + sep + nazwa_czast + ".pdb"
        subprocess.run([self.sc + sep + 'RNAVIEW/bin/rnaview', sc_pliku])

        self.assertTrue(isfile(sc_pliku + ".out") or isfile(sc_pliku + "_nmr.pdb.out"))

        for file in [f for f in listdir('.') if isfile(f) and ((".out" in f) or ("pdb_nmr.pdb" in f))]:
            remove(file)



if __name__ == '__main__':
    unittest.main()
