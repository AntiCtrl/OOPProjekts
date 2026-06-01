import pygame

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
        Logs.blit(Teksts, TekstaVieta)

    # Pārbauda, vai poga ir nospiesta
    def VaiNospiesta(self, Pozicija):
        return self.Taisnsturis.collidepoint(Pozicija)


# === Saskarne =====================================

pygame.init()

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

# Teksta ievades lauks
TekstaLauks = pygame.Rect(300, 320, 400, 60)

# Šeit glabāsies spēlētāja ievadītais vārds
SpeletajaVards = ""

# Šeit glabājas brīdinājuma teksts, ja ievade nav pareiza
Bridinajums = ""

# Glabā spēlētāja izvēlēto kategoriju
IzveletaKategorija = ""

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
        Logs.blit(BridTeksts, (285, 395))

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

                        # Nākamais ekrāns būs grūtības izvēle
                        Ekrans = "grutiba"

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


    if Ekrans == "sakums":
        ParaditSakumaEkranu()

    elif Ekrans == "instrukcija":
        ParaditInstrukcijuLogu()

    elif Ekrans == "vards":
        ParaditVardaIevadi()
    
    elif Ekrans == "kategorija":
        ParaditKategorijasLogu()
    
    # Atjauno ekrāna attēlu
    pygame.display.update()

pygame.quit()