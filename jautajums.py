class Jautajums:
    def __init__(self, teksts="", atbildes=None, pareiza_atbilde="", kategorija="", grutiba=""):
        pass

    def ParaditJautajumu(self):
        pass

    def ParbauditAtbildi(self, atbilde):
        pass

    def GetTeksts(self): pass
    def GetAtbildes(self): pass
    def GetPareizaAtbilde(self): pass
    def GetKategorija(self): pass
    def GetGrutiba(self): pass
    def GetPunktiParPareizu(self): pass
    def GetPunktiParNepareizu(self): pass
    def __del__(self): pass

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