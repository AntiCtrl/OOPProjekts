from datetime import datetime

class Rezultats:
     # klase kas atbild par rezultata save/apstradi
    def __init__(self, vards="", punkti=0, pareizas_atbildes=0, kludas=0, grutiba="", kategorija=""):
        # private dati 
        self.__Vards = vards
        self.__Punkti = punkti
        self.__PareizasAtbildes = pareizas_atbildes
        self.__Kludas = kludas
        self.__Grutiba = grutiba
        self.__Kategorija = kategorija

        # Saglabā rezultāta izveides datumu un laiku
        self.__Datums = datetime.now().strftime("%d.%m.%Y %H:%M")
        
        #  nosaka tekstu atkarībā no iegūtajiem punktiem
        self.__RezultataTeksts = self.NoteiktRezultataTekstu(punkti)
        
    def NoteiktRezultataTekstu(self, punkti):
        if punkti >= 80:
            return "Tu atradi dārgumu!"
        elif punkti >= 50:
            return "Tu biji tuvu tam, lai atrastu dārgumu!"
        else:
            return "Diemžēl tu neatradi dārgumu."

    #get motodes 
    def GetVards(self): return self.__Vards
    def GetPunkti(self): return self.__Punkti
    def GetPareizasAtbildes(self): return self.__PareizasAtbildes
    def GetKludas(self): return self.__Kludas
    def GetGrutiba(self): return self.__Grutiba
    def GetKategorija(self): return self.__Kategorija
    def GetRezultataTeksts(self): return self.__RezultataTeksts
    def GetDatums(self): return self.__Datums


    # izdruka rez konsole testam
    def Paradit(self):
        print("Spēlētājs:", self.__Vards)
        print("Punkti:", self.__Punkti)
        print("Pareizas atbildes:", self.__PareizasAtbildes)
        print("Kategorija:", self.__Kategorija)
        print("Grūtība:", self.__Grutiba)
        print("Kļūdas:", self.__Kludas)
        print("Datums:", self.__Datums)
        print("Rezultāts:", self.__RezultataTeksts)
