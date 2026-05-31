class Kategorija:

    # Konstruktors
    def __init__(self, nosaukums=""):
        self.__Nosaukums = nosaukums

    # Uzstāda kategorijas nosaukumu
    def SetNosaukums(self, nosaukums):
        self.__Nosaukums = nosaukums

    # Atgriež kategorijas nosaukumu
    def GetNosaukums(self):
        return self.__Nosaukums