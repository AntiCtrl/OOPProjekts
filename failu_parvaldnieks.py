import json
import csv
from jautajums import VieglsJautajums, VidejsJautajums, GrutsJautajums

class FailuParvaldnieks:
    # klase kas atbild par visu datu read/write
    def __init__(self, jautajumu_fails="dati/jautajumi.json", rezultatu_fails="dati/rezultati.csv"):
        self.__JautajumuFails = jautajumu_fails
        self.__RezultatuFails = rezultatu_fails

    # nolasa jautājumus no jsona un izveido klases objektus
    def NolasitJautajumus(self, kategorija, grutiba):
        Fails = open(self.__JautajumuFails, "r", encoding="utf-8")
        Teksts = Fails.read()
        Fails.close()

        Dati = json.loads(Teksts)
        Jautajumi = []  #  saraksts 

        # atlasa tikai tos jautājumus kas atbilst  kategorijai un grutibai
        for ieraksts in Dati:
            if ieraksts["kategorija"] == kategorija and ieraksts["grutiba"] == grutiba:
                Teksts = ieraksts["jautajums"]
                Atbildes = ieraksts["atbildes"]
                Pareiza = ieraksts["pareiza"]

                # izveido pareizo apaksklasi, balstoties uz grutibu // polimorfisms
                if grutiba == "Viegls":
                    Jautajumi.append(VieglsJautajums(Teksts, Atbildes, Pareiza, kategorija))
                elif grutiba == "Vidējs":
                    Jautajumi.append(VidejsJautajums(Teksts, Atbildes, Pareiza, kategorija))
                else:
                    Jautajumi.append(GrutsJautajums(Teksts, Atbildes, Pareiza, kategorija))

        return Jautajumi

    # beigu rezultats tiek pievienots csv faila 
    def SaglabatRezultatu(self, rezultats):
        Fails = open(self.__RezultatuFails, "a", encoding="utf-8", newline="")
        Rakstitajs = csv.writer(Fails)
        Rakstitajs.writerow([
            rezultats.GetVards(), rezultats.GetPunkti(), rezultats.GetPareizasAtbildes(),
            rezultats.GetKludas(), rezultats.GetKategorija(), rezultats.GetGrutiba(),
            rezultats.GetRezultataTeksts()
        ])
        Fails.close()

    # nolasa visus ieprieksejos rezultatus lai parādītu tos tabulā
    def NolasitRezultatus(self):
        Rezultati = []
        try:
            Fails = open(self.__RezultatuFails, "r", encoding="utf-8")
            Lasitajs = csv.reader(Fails)
            for rinda in Lasitajs:
                Rezultati.append(rinda)
            Fails.close()
        except:
            pass # ja faila nav atgriez tuksu sarakstu
        return Rezultati

    # parbauda vai csv eksiste, ja ne izveido to un ieraksta kolonnu nosaukumus
    def IzveidotRezultatuFailuJaVajag(self):
        try:
            Fails = open(self.__RezultatuFails, "r", encoding="utf-8")
            Fails.close()
        except:
            Fails = open(self.__RezultatuFails, "w", encoding="utf-8", newline="")
            Rakstitajs = csv.writer(Fails)
            Rakstitajs.writerow(["Vards", "Punkti", "Pareizi", "Kludas", "Kategorija", "Grutiba", "Dargums"])
            Fails.close()
