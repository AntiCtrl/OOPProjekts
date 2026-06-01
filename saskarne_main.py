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

                        if poga.Teksts == "Spēles noteikumi":
                            Ekrans = "instrukcija"

                        if poga.Teksts == "Iziet":
                            Darbojas = False

            elif Ekrans == "instrukcija":

                if AtpakalPoga.VaiNospiesta(Pozicija):
                    Ekrans = "sakums"

    if Ekrans == "sakums":
        ParaditSakumaEkranu()

    elif Ekrans == "instrukcija":
        ParaditInstrukcijuLogu()
    
    # Atjauno ekrāna attēlu
    pygame.display.update()

pygame.quit()