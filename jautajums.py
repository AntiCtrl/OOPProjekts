class Jautajums:
    # klase kas glaba info par vienu question
    def __init__(self, teksts="", atbildes=None, pareiza_atbilde="", kategorija="", grutiba=""):
        #aizsargatie dati lai atvasinatas klases var tiem pieklut
        self._Teksts = teksts
        if atbildes is None:
            self._Atbildes = []
        else:
            self._Atbildes = atbildes
        self._PareizaAtbilde = pareiza_atbilde
        self._Kategorija = kategorija
        self._Grutiba = grutiba
        
        
    def ParaditJautajumu(self):
        print(self._Teksts)
        for i in range(len(self._Atbildes)):
            print(str(i + 1) + ".", self._Atbildes[i])

    # virtuala funkcija/ parbauda vai izvele sakrit ar pareizo atbildi
    def ParbauditAtbildi(self, atbilde):
        return atbilde == self._PareizaAtbilde

        #get metodes, lai iegutu private datus
    def GetTeksts(self): return self._Teksts
    def GetAtbildes(self): return self._Atbildes
    def GetPareizaAtbilde(self): return self._PareizaAtbilde
    def GetKategorija(self): return self._Kategorija
    def GetGrutiba(self): return self._Grutiba

    # virtuālās metodes, kuras tiek pārdefinētas atvasinātajās klasēs
    def GetPunktiParPareizu(self):
        return 0

    def GetPunktiParNepareizu(self):
        return 0

    #atvasinatas klases, kuras manto visu no "Jautajums" klases
class VieglsJautajums(Jautajums):
    def __init__(self, teksts="", atbildes=None, pareiza_atbilde="", kategorija=""):
        super().__init__(teksts, atbildes, pareiza_atbilde, kategorija, "Viegls")

    def GetPunktiParPareizu(self): return 10
    def GetPunktiParNepareizu(self): return 5

class VidejsJautajums(Jautajums):
    def __init__(self, teksts="", atbildes=None, pareiza_atbilde="", kategorija=""):
        super().__init__(teksts, atbildes, pareiza_atbilde, kategorija, "Vidējs")

    def GetPunktiParPareizu(self): return 10
    def GetPunktiParNepareizu(self): return 5

class GrutsJautajums(Jautajums):
    def __init__(self, teksts="", atbildes=None, pareiza_atbilde="", kategorija=""):
        super().__init__(teksts, atbildes, pareiza_atbilde, kategorija, "Grūts")

    def GetPunktiParPareizu(self): return 10
    def GetPunktiParNepareizu(self): return 5
