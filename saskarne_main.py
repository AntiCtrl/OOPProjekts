import pygame
from spele import Spele

# === Poga =========================================
class Poga:

    # Konstruktors -  izveido jaunu pogu ar norādīto pozīciju, izmēru un tekstu
    def __init__(self, x, y, platums, augstums, teksts):
        self.X = x
        self.Y = y
        self.Platums = platums
        self.Augstums = augstums
        self.Teksts = teksts
        self.Taisnsturis = pygame.Rect(x, y, platums, augstums)

    # Parāda pogu uz ekrāna
    def Paradit(self, Logs, Fonts):
        PeleX, PeleY = pygame.mouse.get_pos() # iegūst peles pašreizējo pozīciju

        if self.Taisnsturis.collidepoint(PeleX, PeleY):
            Krasa = pygame.Color("#D4FF5E") # pogas krāsa, kad pele atrodas virs tās
        else:
            Krasa = pygame.Color("#C6FFA3") # pogas parastā krāsa
            
        pygame.draw.rect(Logs, Krasa, self.Taisnsturis, border_radius=15)
        pygame.draw.rect(Logs, pygame.Color("#74C214"), self.Taisnsturis, width=3, border_radius=15)

        Teksts = Fonts.render(self.Teksts, True, (0, 0, 0))
        TekstaVieta = Teksts.get_rect(center=self.Taisnsturis.center)
        Logs.blit(Teksts, TekstaVieta) # blit() kopē attēlu vai tekstu uz spēles logu noteiktā pozīcijā.

    # Pārbauda, vai poga ir nospiesta
    def VaiNospiesta(self, Pozicija):
        return self.Taisnsturis.collidepoint(Pozicija)


# === Saskarne =====================================

pygame.init()
SpelesObjekts = Spele()

Platums = 1000
Augstums = 650

# izveido programmas logu
Logs = pygame.display.set_mode((Platums, Augstums)) 
pygame.display.set_caption("Dārgumu Medības Džungļos")

Fonts = pygame.font.SysFont("comicsansms", 30, bold=True)
MazsFonts = pygame.font.SysFont("comicsansms", 18)

Fons = pygame.image.load("assets/fons.png")
Fons = pygame.transform.scale(Fons, (Platums, Augstums))

Karte = pygame.image.load("assets/karte.png")
Karte = pygame.transform.scale(Karte, (800, 400))

Pogas = [
    Poga(350, 250, 300, 60, "Spēlēt"),
    Poga(350, 320, 300, 60, "Spēles noteikumi"),
    Poga(350, 390, 300, 60, "Rezultāti"),
    Poga(350, 460, 300, 60, "Iziet")
]

AtpakalPoga = Poga(40, 550, 170, 55, "Atpakaļ")
TurpinatPoga = Poga(790, 550, 170, 55, "Turpināt")

KategorijuPogas = [
    Poga(160, 280, 210, 60, "Kultūra"),
    Poga(390, 280, 210, 60, "Vēsture"),
    Poga(620, 280, 210, 60, "Sports"),

    Poga(265, 380, 210, 60, "Ģeogrāfija"),
    Poga(515, 380, 210, 60, "Matemātika")
]

GrutibasPogas = [
    Poga(160, 290, 200, 60, "Viegls"),
    Poga(390, 290, 200, 60, "Vidējs"),
    Poga(620, 290, 200, 60, "Grūts")
]

AtbilzuPogas = [
    Poga(230, 380, 240, 55, "Rīga"),
    Poga(530, 380, 240, 55, "Liepāja"),
    Poga(230, 455, 240, 55, "Ventspils"),
    Poga(530, 455, 240, 55, "Daugavpils")
]

IzvelnePoga = Poga(650, 550, 300, 55, "Atgriezties izvēlnē")

# Teksta ievades lauks
TekstaLauks = pygame.Rect(300, 320, 400, 60)

# Šeit glabāsies spēlētāja ievadītais vārds
SpeletajaVards = ""

# Šeit glabājas brīdinājuma teksts, ja ievade nav pareiza
Bridinajums = ""

# Glabā spēlētāja izvēlēto kategoriju
IzveletaKategorija = ""

# Glabā spēlētāja izvēlēto grūtības līmeni
IzveletaGrutiba = ""

Ekrans = "sakums"
Darbojas = True # mainīgais, kas kontrolē programmas darbību


# Parāda sākuma ekrānu
def ParaditSakumaEkranu():
    Logs.blit(Fons, (0, 0))

    for poga in Pogas:
        poga.Paradit(Logs, Fonts)


# Parāda instrukciju logu
def ParaditInstrukcijuLogu():
    Logs.blit(Fons, (0, 0))

    # Parāda karti instrukcijas fonā
    Logs.blit(Karte, (100, 150))

    Virsraksts = Fonts.render("Spēles noteikumi", True, pygame.Color("#000000"))
    Logs.blit(Virsraksts, (190, 195))

    Instrukcija = [
        "1. Ievadi savu vārdu.",
        "2. Izvēlies jautājumu kategoriju un grūtības līmeni.",
        "3. Atbildi uz 10 jautājumiem, katram izvēloties vienu no 4 atbilžu variantiem.",
        "4. Par katru pareizu atbildi iegūsi 10 punktus.",
        "5. Par katru nepareizu atbildi zaudēsi 5 punktus.",
        "6. Punktu skaits nevar kļūt mazāks par 0.",
        "7. Spēles beigās redzēsi savu rezultātu un uzzināsi, vai atradi dārgumu.",
        "",
        "Veiksmi dārgumu medībās!"
    ]

    y = 250

    # Pa vienai rindai parāda instrukcijas tekstu
    for rinda in Instrukcija:
        Teksts = MazsFonts.render(rinda, True, pygame.Color("#000000"))
        Logs.blit(Teksts, (190, y))
        y += 28

    AtpakalPoga.Paradit(Logs, Fonts)


# Parāda vārda ievades logu
def ParaditVardaIevadi():
    Logs.blit(Fons, (0, 0))

    # Parāda karti kā fonu ievades logam
    Logs.blit(Karte, (100, 150))

    Virsraksts = Fonts.render("Ievadi savu vārdu:", True, pygame.Color("#000000"))
    VirsrakstaVieta = Virsraksts.get_rect(center=(Platums // 2, 250))
    Logs.blit(Virsraksts, VirsrakstaVieta)

    # Uzzīmē teksta ievades lauku
    pygame.draw.rect(Logs, pygame.Color("#FFF4C7"), TekstaLauks, border_radius=10)
    pygame.draw.rect(Logs, pygame.Color("#74C214"), TekstaLauks, width=3, border_radius=10)

    # Parāda lietotāja ievadīto tekstu
    Teksts = Fonts.render(SpeletajaVards, True, pygame.Color("#000000"))
    Logs.blit(Teksts, (TekstaLauks.x + 15, TekstaLauks.y + 10))
    
    # Ja ir kļūda ievadē, parāda brīdinājumu
    if Bridinajums != "":
        BridTeksts = MazsFonts.render(Bridinajums, True, pygame.Color("#FF0000"))
        Logs.blit(BridTeksts, (300, 395))

    AtpakalPoga.Paradit(Logs, Fonts)
    TurpinatPoga.Paradit(Logs, Fonts)

# Parāda kategorijas izvēles logu
def ParaditKategorijasLogu():
    Logs.blit(Fons, (0, 0))
    Logs.blit(Karte, (100, 150))

    Virsraksts = Fonts.render("Izvēlies kategoriju", True, pygame.Color("#000000"))
    VirsrakstaVieta = Virsraksts.get_rect(center=(Platums // 2, 230))

    Logs.blit(Virsraksts, VirsrakstaVieta)

    for poga in KategorijuPogas:
        poga.Paradit(Logs, Fonts)

    AtpakalPoga.Paradit(Logs, Fonts)

# Parāda grūtības līmeņa izvēles logu
def ParaditGrutibasLogu():
    Logs.blit(Fons, (0, 0))
    Logs.blit(Karte, (100, 150))

    Virsraksts = Fonts.render("Izvēlies grūtības līmeni", True, pygame.Color("#000000"))
    VirsrakstaVieta = Virsraksts.get_rect(center=(Platums // 2, 230))
    Logs.blit(Virsraksts, VirsrakstaVieta)

    for poga in GrutibasPogas:
        poga.Paradit(Logs, Fonts)

    AtpakalPoga.Paradit(Logs, Fonts)


# Parāda spēles logu
def ParaditSpelesLogu():
    Logs.blit(Fons, (0, 0))
    Logs.blit(Karte, (100, 150))

    Speletajs = SpelesObjekts.GetSpeletajs()

    # Augšējā informācija
    Info1 = MazsFonts.render("Spēlētājs: " + Speletajs.GetVards(), True, pygame.Color("#000000"))
    Logs.blit(Info1, (180, 190))

    Info2 = MazsFonts.render("Punkti: " + str(Speletajs.GetPunkti()), True, pygame.Color("#000000"))
    Logs.blit(Info2, (680, 190))

    Info3 = MazsFonts.render("Kategorija: " + Speletajs.GetKategorija(), True, pygame.Color("#000000"))
    Logs.blit(Info3, (180, 220))

    Info4 = MazsFonts.render("Grūtība: " + Speletajs.GetGrutiba(), True, pygame.Color("#000000"))
    Logs.blit(Info4, (680, 220))

    # Jautājuma numurs
    JautajumaNr = Fonts.render(
        "Jautājums " + str(SpelesObjekts.GetJautajumaNr() + 1) + "/" + str(SpelesObjekts.GetJautajumuSkaits()),
        True, pygame.Color("#000000"))
    JautajumaNrVieta = JautajumaNr.get_rect(center=(Platums // 2, 270))
    Logs.blit(JautajumaNr, JautajumaNrVieta)

    # Pašreizējais jautājums
    Jautajums = SpelesObjekts.GetCurrentJautajums()

    if Jautajums is not None:

        JautajumaTeksts = MazsFonts.render(Jautajums.GetTeksts(), True, pygame.Color("#000000"))
        JautajumaVieta = JautajumaTeksts.get_rect(center=(Platums // 2, 330))
        Logs.blit(JautajumaTeksts, JautajumaVieta)

        Atbildes = Jautajums.GetAtbildes()

        for i in range(len(Atbildes)):
            AtbilzuPogas[i].Teksts = Atbildes[i]
            AtbilzuPogas[i].Paradit(Logs, MazsFonts)

    AtpakalPoga.Paradit(Logs, Fonts)

# Parāda spēles rezultātu logu
def ParaditRezultatuLogu():
    Logs.blit(Fons, (0, 0))
    Logs.blit(Karte, (100, 150))

    Rezultats = SpelesObjekts.GetRezultats()

    Virsraksts = Fonts.render("SPĒLES REZULTĀTS", True, pygame.Color("#000000"))
    VirsrakstaVieta = Virsraksts.get_rect(center=(Platums // 2, 230))
    Logs.blit(Virsraksts, VirsrakstaVieta)

    Teksts1 = MazsFonts.render("Spēlētājs: " + Rezultats.GetVards(), True, pygame.Color("#000000"))
    Logs.blit(Teksts1, (400, 260))

    Teksts2 = MazsFonts.render("Kategorija: " + Rezultats.GetKategorija(), True, pygame.Color("#000000"))
    Logs.blit(Teksts2, (400, 290))

    Teksts3 = MazsFonts.render("Grūtība: " + Rezultats.GetGrutiba(), True, pygame.Color("#000000"))
    Logs.blit(Teksts3, (400, 320))

    Teksts4 = MazsFonts.render("Punkti: " + str(Rezultats.GetPunkti()), True, pygame.Color("#000000"))
    Logs.blit(Teksts4, (400, 365))

    Teksts5 = MazsFonts.render("Pareizas atbildes: " + str(Rezultats.GetPareizasAtbildes()), True, pygame.Color("#000000"))
    Logs.blit(Teksts5, (400, 395))

    Teksts6 = MazsFonts.render("Kļūdas: " + str(Rezultats.GetKludas()), True, pygame.Color("#000000"))
    Logs.blit(Teksts6, (400, 425))

    RezultataTeksts = MazsFonts.render(Rezultats.GetRezultataTeksts(), True, pygame.Color("#000000"))
    RezultataVieta = RezultataTeksts.get_rect(center=(Platums // 2, 480))
    Logs.blit(RezultataTeksts, RezultataVieta)

    IzvelnePoga.Paradit(Logs, Fonts)

# Parāda visu spēlētāju rezultātu tabulu
def ParaditRezultatuTabulu():

    Logs.blit(Fons, (0, 0))
    Logs.blit(Karte, (100, 150))

    Virsraksts = Fonts.render("REZULTĀTI", True, pygame.Color("#000000"))
    VirsrakstaVieta = Virsraksts.get_rect(center=(Platums // 2, 230))
    Logs.blit(Virsraksts, VirsrakstaVieta)

    xDatums = 170
    xVards = 330
    xPunkti = 470
    xPareizi = 560
    xKludas = 670

    y = 260

    Logs.blit(MazsFonts.render("Datums un laiks", True, pygame.Color("#000000")), (xDatums, y))
    Logs.blit(MazsFonts.render("Vārds", True, pygame.Color("#000000")), (xVards, y))
    Logs.blit(MazsFonts.render("Punkti", True, pygame.Color("#000000")), (xPunkti, y))
    Logs.blit(MazsFonts.render("Pareizi", True, pygame.Color("#000000")), (xPareizi, y))
    Logs.blit(MazsFonts.render("Kļūdas", True, pygame.Color("#000000")), (xKludas, y))

    Rezultati = SpelesObjekts.NolasitRezultatus()

    # Izlaiž pirmo rindu, jo tur ir kolonnu nosaukumi
    if len(Rezultati) > 0:
        Rezultati = Rezultati[1:]

    # Parāda tikai pēdējos 4 rezultātus
    Rezultati = Rezultati[-4:]
    Rezultati.reverse()

    y = 310

    for rezultats in Rezultati:

        if len(rezultats) >= 8:
            Logs.blit(MazsFonts.render(rezultats[0], True, pygame.Color("#000000")), (xDatums, y))
            Logs.blit(MazsFonts.render(rezultats[1], True, pygame.Color("#000000")), (xVards, y))
            Logs.blit(MazsFonts.render(rezultats[2], True, pygame.Color("#000000")), (xPunkti, y))
            Logs.blit(MazsFonts.render(rezultats[3], True, pygame.Color("#000000")), (xPareizi, y))
            Logs.blit(MazsFonts.render(rezultats[4], True, pygame.Color("#000000")), (xKludas, y))

            y += 40

    AtpakalPoga.Paradit(Logs, Fonts)

while (Darbojas == True):

    for Event in pygame.event.get():

        if Event.type == pygame.QUIT:
            Darbojas = False

        # Lietotājs nospiež peles pogu
        if Event.type == pygame.MOUSEBUTTONDOWN:
            Pozicija = Event.pos  # Saglabā peles pozīciju

            if Ekrans == "sakums":

                for poga in Pogas:
                    if poga.VaiNospiesta(Pozicija):
                        print("Nospiesta poga:", poga.Teksts)

                        if poga.Teksts == "Spēlēt":
                            Ekrans = "vards"
                        
                        if poga.Teksts == "Rezultāti":
                            Ekrans = "rezultatu_tabula"

                        if poga.Teksts == "Spēles noteikumi":
                            Ekrans = "instrukcija"

                        if poga.Teksts == "Iziet":
                            Darbojas = False

            elif Ekrans == "instrukcija":

                if AtpakalPoga.VaiNospiesta(Pozicija):
                    Ekrans = "sakums"

            elif Ekrans == "vards":

                if AtpakalPoga.VaiNospiesta(Pozicija):
                    Ekrans = "sakums"

                if TurpinatPoga.VaiNospiesta(Pozicija):

                    if SpeletajaVards == "":
                        Bridinajums = "Lūdzu, ievadiet savu vārdu!"

                    elif len(SpeletajaVards) > 20:
                        Bridinajums = "Vārds nedrīkst būt garāks par 20 simboliem!"

                    else:
                        Bridinajums = ""
                        print("Spēlētāja vārds:", SpeletajaVards)
                        Ekrans = "kategorija"

            elif Ekrans == "kategorija":

                if AtpakalPoga.VaiNospiesta(Pozicija):
                    Ekrans = "vards"

                for poga in KategorijuPogas:
                    if poga.VaiNospiesta(Pozicija):
                        IzveletaKategorija = poga.Teksts
                        print("Izvēlētā kategorija:", IzveletaKategorija)

                        # Pēc kategorijas izvēles pāriet uz grūtības izvēli
                        Ekrans = "grutiba"

            elif Ekrans == "grutiba":

                if AtpakalPoga.VaiNospiesta(Pozicija):
                    Ekrans = "kategorija"

                for poga in GrutibasPogas:
                    if poga.VaiNospiesta(Pozicija):
                        IzveletaGrutiba = poga.Teksts
                        print("Izvēlētā grūtība:", IzveletaGrutiba)

                        # Sāk spēli ar izvēlēto vārdu, kategoriju un grūtību
                        SpelesObjekts.SaktSpeli(SpeletajaVards, IzveletaKategorija, IzveletaGrutiba)
                        
                        Ekrans = "spele"

            elif Ekrans == "spele":

                if AtpakalPoga.VaiNospiesta(Pozicija):
                    Ekrans = "grutiba"

                for poga in AtbilzuPogas:
                    if poga.VaiNospiesta(Pozicija):
                        print("Izvēlētā atbilde:", poga.Teksts)

                        SpelesObjekts.ParbauditAtbildi(poga.Teksts)

                        if SpelesObjekts.VaiSpeleBeigusies():
                            SpelesObjekts.BeigtSpeli()
                            Ekrans = "rezultats"

            elif Ekrans == "rezultats":

                if IzvelnePoga.VaiNospiesta(Pozicija):
                    SpeletajaVards = ""
                    IzveletaKategorija = ""
                    IzveletaGrutiba = ""
                    Bridinajums = ""
                    Ekrans = "sakums"

            elif Ekrans == "rezultatu_tabula":

                if AtpakalPoga.VaiNospiesta(Pozicija):
                    Ekrans = "sakums"

        # Lietotājs ievada tekstu ar klaviatūru
        if Event.type == pygame.KEYDOWN:

            if Ekrans == "vards":

                # Backspace dzēš pēdējo simbolu
                if Event.key == pygame.K_BACKSPACE:
                    SpeletajaVards = SpeletajaVards[:-1]
                    Bridinajums = ""

                # Enter darbojas tāpat kā poga Turpināt
                elif Event.key == pygame.K_RETURN:

                    if SpeletajaVards == "":
                        Bridinajums = "Lūdzu, ievadiet savu vārdu!"

                    elif len(SpeletajaVards) > 20:
                        Bridinajums = "Vārds nedrīkst būt garāks par 20 simboliem!"

                    else:
                        Bridinajums = ""
                        print("Spēlētāja vārds:", SpeletajaVards)
                        Ekrans = "kategorija"

                else:
                    SpeletajaVards += Event.unicode
                    Bridinajums = ""

    # зārbauda, kurš ekrāns pašlaik ir aktīvs, un attēlo atbilstošo logu
    if Ekrans == "sakums":
        ParaditSakumaEkranu()

    elif Ekrans == "instrukcija":
        ParaditInstrukcijuLogu()

    elif Ekrans == "vards":
        ParaditVardaIevadi()
    
    elif Ekrans == "kategorija":
        ParaditKategorijasLogu()
    
    elif Ekrans == "grutiba":
        ParaditGrutibasLogu()
    
    elif Ekrans == "spele":
        ParaditSpelesLogu()
    
    elif Ekrans == "rezultats":
        ParaditRezultatuLogu()

    elif Ekrans == "rezultatu_tabula":
        ParaditRezultatuTabulu()
    
    # Atjauno ekrāna attēlu
    pygame.display.update()

pygame.quit()