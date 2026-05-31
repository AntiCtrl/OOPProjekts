class Speletajs:

    # Konstruktors
    def __init__(self, vards=""):
        self.__Vards = vards
        self.__Punkti = 0
        self.__PareizasAtbildes = 0
        self.__Kludas = 0
        self.__Grutiba = ""
        self.__Kategorija = ""

    # Uzstāda spēlētāja vārdu
    def SetVards(self, vards):
        self.__Vards = vards

    # Atgriež spēlētāja vārdu
    def GetVards(self):
        return self.__Vards

    # Uzstāda grūtības līmeni
    def SetGrutiba(self, grutiba):
        self.__Grutiba = grutiba

    # Atgriež grūtības līmeni
    def GetGrutiba(self):
        return self.__Grutiba

    # Uzstāda kategoriju
    def SetKategorija(self, kategorija):
        self.__Kategorija = kategorija

    # Atgriež kategoriju
    def GetKategorija(self):
        return self.__Kategorija

    # Pievieno punktus
    def PievienotPunktus(self, punkti):
        self.__Punkti += punkti

    # Noņem punktus
    def AtnemtPunktus(self, punkti):
        self.__Punkti -= punkti

        # Punkti nevar būt mazāki par 0
        if self.__Punkti < 0:
            self.__Punkti = 0

    # Atgriež punktu skaitu
    def GetPunkti(self):
        return self.__Punkti

    # Palielina pareizo atbilžu skaitu
    def PievienotPareizuAtbildi(self):
        self.__PareizasAtbildes += 1

    # Palielina kļūdu skaitu
    def PievienotKludu(self):
        self.__Kludas += 1

    # Atgriež pareizo atbilžu skaitu
    def GetPareizasAtbildes(self):
        return self.__PareizasAtbildes

    # Atgriež kļūdu skaitu
    def GetKludas(self):
        return self.__Kludas