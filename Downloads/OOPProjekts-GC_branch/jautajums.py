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

    # noklusejuma punkti atvasinatas klases tos velak paraksta
    def GetPunktiParPareizu(self): pass
    def GetPunktiParNepareizu(self): pass
    def __del__(self): pass

    #atvasinatas klases, kuras manto visu no "Jautajums" klases
class VieglsJautajums(Jautajums):
    def __init__(self, teksts="", atbildes=None, pareiza_atbilde="", kategorija=""):
        pass
    def GetPunktiParPareizu(self): pass
    def GetPunktiParNepareizu(self): pass

class VidejsJautajums(Jautajums):
    def __init__(self, teksts="", atbildes=None, pareiza_atbilde="", kategorija=""):
        pass
    def GetPunktiParPareizu(self): pass
    def GetPunktiParNepareizu(self): pass

class GrutsJautajums(Jautajums):
    def __init__(self, teksts="", atbildes=None, pareiza_atbilde="", kategorija=""):
        pass
    def GetPunktiParPareizu(self): pass
    def GetPunktiParNepareizu(self): pass