from speletajs import Speletajs
from kategorija import Kategorija
from rezultats import Rezultats
from failu_parvaldnieks import FailuParvaldnieks

class Spele:
    # galvena klase kas parvalda speles gaitu un savieno visu
    def __init__(self):
        self.__Speletajs = Speletajs()
        
        # Saraksts ar pieejamajām kategorijām
        self.__Kategorijas = []
        self.__Kategorijas.append(Kategorija(1, "Kultūra", "Jautājumi par kultūru"))
        self.__Kategorijas.append(Kategorija(2, "Vēsture", "Jautājumi par vēsturi"))
        self.__Kategorijas.append(Kategorija(3, "Sports", "Jautājumi par sportu"))
        self.__Kategorijas.append(Kategorija(4, "Ģeogrāfija", "Jautājumi par ģeogrāfiju"))
        self.__Kategorijas.append(Kategorija(5, "Matemātika", "Jautājumi par matemātiku"))

        self.__Jautajumi = [] 
        self.__JautajumaNr = 0
        self.__FailuParvaldnieks = FailuParvaldnieks()
        self.__Rezultats = None
        self.__FailuParvaldnieks.IzveidotRezultatuFailuJaVajag()

    # sak jaunu speli, piefikse izveles un reado jautajumus no faila
    def SaktSpeli(self, vards, kategorija, grutiba):
        self.__Speletajs = Speletajs(vards)
        self.__Speletajs.SetKategorija(kategorija)
        self.__Speletajs.SetGrutiba(grutiba)
        self.__JautajumaNr = 0
        self.__Jautajumi = self.__FailuParvaldnieks.NolasitJautajumus(kategorija, grutiba)

    def GetSpeletajs(self): return self.__Speletajs
    def GetKategorijas(self): return self.__Kategorijas
    def GetJautajumaNr(self): return self.__JautajumaNr
    def GetJautajumuSkaits(self): return len(self.__Jautajumi)

    # iedod to jautajumu, pie kura speletajs atrodas
    def GetCurrentJautajums(self):
        if self.__JautajumaNr < len(self.__Jautajumi):
            return self.__Jautajumi[self.__JautajumaNr]
        else:
            return None

    # parbauda atbildi + - punkuts
    def ParbauditAtbildi(self, atbilde):
        Jautajums = self.GetCurrentJautajums()
        if Jautajums is None:
            return False

        if Jautajums.ParbauditAtbildi(atbilde):
            self.__Speletajs.PievienotPunktus(Jautajums.GetPunktiParPareizu())
            self.__Speletajs.PievienotPareizuAtbildi()
            Pareizi = True
        else:
            self.__Speletajs.AtnemtPunktus(Jautajums.GetPunktiParNepareizu())
            self.__Speletajs.PievienotKludu()
            Pareizi = False

        self.__JautajumaNr += 1 
        return Pareizi

    # parbauda vai jautajumi beidzas
    def VaiSpeleBeigusies(self):
        return self.__JautajumaNr >= len(self.__Jautajumi)

    # beigas izveido rez un saglaba csv faila
    def BeigtSpeli(self):
        self.__Rezultats = Rezultats(
            self.__Speletajs.GetVards(),
            self.__Speletajs.GetPunkti(),
            self.__Speletajs.GetPareizasAtbildes(),
            self.__Speletajs.GetKludas(),
            self.__Speletajs.GetGrutiba(),
            self.__Speletajs.GetKategorija()
        )
        self.__FailuParvaldnieks.SaglabatRezultatu(self.__Rezultats)
        return self.__Rezultats

    def GetRezultats(self): return self.__Rezultats
    def NolasitRezultatus(self): return self.__FailuParvaldnieks.NolasitRezultatus()
