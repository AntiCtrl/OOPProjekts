class Kategorija:

    def __init__(self, id=0, nosaukums="", apraksts=""):
        self.__Id = id
        self.__Nosaukums = nosaukums
        self.__Apraksts = apraksts

    def GetId(self):
        return self.__Id

    def GetNosaukums(self):
        return self.__Nosaukums

    def GetApraksts(self):
        return self.__Apraksts